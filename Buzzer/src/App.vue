<template>
  <div>
    <div class="piano-title">
      Play here !
    </div>
    <div class="piano">
      <div v-for="note in notes" :key="note">
        <button @click="jouerNote(note)">{{ note.name }}</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      // notes: ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C5'],
      notes: [{ name: 'C', freq: 261 }, { name: 'D', freq: 294 }, { name: 'E', freq: 329 }, { name: 'F', freq: 349 }, { name: 'G', freq: 392 }, { name: 'A', freq: 440 }, { name: 'B', freq: 493 }, { name: 'C5', freq: 523 }]
    }
  },
  methods: {
    async jouerNote(note) {
     await fetch('http://localhost:3000/play', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },  
        body: JSON.stringify({ note })
      })
    }
  },
  mounted() {
    window.addEventListener('keydown', (event) => {
      switch (event.key) {
        case 'a':
          this.jouerNote(this.notes[0])
          break
        case 'z':
          this.jouerNote(this.notes[1])
          break
        case 'e':
          this.jouerNote(this.notes[2])
          break
        case 'r':
          this.jouerNote(this.notes[3])
          break
        case 't':
          this.jouerNote(this.notes[4])
          break
        case 'y':
          this.jouerNote(this.notes[5])
          break
        case 'u':
          this.jouerNote(this.notes[6])
          break
        case 'i':
          this.jouerNote(this.notes[7])
          break
      }
    })
  }
}
</script>

<style>

.piano {
  display: flex;
  justify-content: center;
}

.piano-title{
    color: white;
    font-size: 34px;
    margin-bottom: 87px;
    display: flex;
    align-items: center;
    justify-content: center;
}

button {
  width: 50px;
  height: 200px;
  background-color: white;
}

button:hover{
  background-color: rgb(203, 203, 203);
}

</style>