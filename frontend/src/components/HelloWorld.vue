<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <p>
      <ul>
        <li>Número de elementos del array: </li>
        <li><input v-model="num_elementos" type="number" placeholder="Introduzca un número"></li>
        <li><button v-on:click="generate_array(num_elementos)">Generar array</button></li>
      </ul>
    </p>

    <div v-if="array_inicial.length!=0">
      <p>
        <ul>
          <li>Array inicial:</li>
          <li>{{array_inicial}}</li>
        </ul>
      </p>
      <p>
        <ul>
          <li><button v-on:click="all_methods()">Ordenar Array</button></li>
        </ul>
      </p>
    </div>
    <!--
    <h3>Métodos</h3>
    <p>
      <ul>
          <li><button v-on:click="burbuja()">Burbuja</button></li>
          <li>{{array_metodo_burbuja}}</li>
      </ul>
        <p>
    </p>
      <ul>
          <li><button v-on:click="quicksort">Quicksort</button></li>
          <li>{{array_metodo_quicksort}}</li>
      </ul>
    </p>
    -->

    <div v-if="lista.length !=0">
      <p>
          <ul>
            <li>
              <div class="container">
                <table class="table" border="">
                  <thead>
                    <th>Método</th>
                    <th>Array ordenado</th>
                    <th>Tiempo empleado (Segundos)</th>
                  </thead>
                  <tbody>
                    <tr v-for="item in lista" v-bind:key="item">
                      <td v-text="item.metodo"></td>
                      <td v-text="item.array_final"></td>
                      <td v-text="item.tiempo"></td>
                  </tr>
                  </tbody>
                </table>
              </div>
          </li>
        </ul>
      </p>
          <ul>
            <li>
              <h3>Clasificación de Tiempos</h3>
              <p v-for="item2 in lista_clasificacion" v-bind:key="item2">Método {{item2.metodo}}: {{item2.tiempo}} s </p>
            </li>
          </ul>
    </div>

  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data(){
    return {
      array_metodo_burbuja : [],
      array_metodo_quicksort : [],
      metodo_burbuja2 : [],
      array_inicial : [],
      num_elementos : [],
      lista : [],
      lista_clasificacion : []
    }
  },
  methods: {
    burbuja: async function () {
      const requestOptions = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ array_inicial: this.array_inicial })
      };
      var response = await fetch('http://127.0.0.1:8000/api/algoritmos/burbuja/', requestOptions);
      this.array_metodo_burbuja = await response.json();
    },
    quicksort: async function () {
      const requestOptions = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ array_inicial: this.array_inicial })
      };
      var response = await fetch('http://127.0.0.1:8000/api/algoritmos/quicksort/', requestOptions);
      this.array_metodo_quicksort = await response.json();
    },
    all_methods: async function () {
      const requestOptions = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ array_inicial: this.array_inicial })
      };
      var response = await fetch('http://127.0.0.1:8000/api/algoritmos/all_methods/', requestOptions);
      this.lista = await response.json();
      this.lista_clasificación = JSON.parse( JSON.stringify( this.lista ) );
      this.generar_clasificacion()
    },
    generate_array: function (n) {
      if(this.num_elementos == 0)
        alert("Introduzca un número válido");
      else{
        this.array_inicial = []
        for (let step = 0; step < n; step++) {
          this.array_inicial.push(this.generar_num_aleatorio())
        }
      }
    },
    generar_num_aleatorio: function () {
      let limite_superior = 250
      let limite_inferior = 0

      return Math.round(Math.random()*(limite_superior-limite_inferior)+parseInt(limite_inferior))
    },
    sortJSON(data, key, orden) {
      return data.sort(function (a, b) {
          var x = a[key],
          y = b[key];

          if (orden === 'asc') {
              return ((x < y) ? -1 : ((x > y) ? 1 : 0));
          }

          if (orden === 'desc') {
              return ((x > y) ? -1 : ((x < y) ? 1 : 0));
          }
      })
    },
    generar_clasificacion: function () {
      var lista_aux  = JSON.parse( JSON.stringify( this.lista ) );
      this.sortJSON(lista_aux, 'tiempo', 'asc');
      this.lista_clasificacion = lista_aux;
    }
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
