<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const reportesRecientes = ref([])

// Datos simulados de los cuestionarios completados por los estudiantes
onMounted(() => {
  reportesRecientes.value = [
    { id: 101, estudiante: 'Martina López', fecha: '2026-09-05', perfil: 'Lógico-Analítico', recomendacion: 'Licenciatura en Sistemas', afinidad: '94%' },
    { id: 102, estudiante: 'Tomás Gómez', fecha: '2026-09-05', perfil: 'Ciencias Exactas', recomendacion: 'Ingeniería', afinidad: '88%' },
    { id: 103, estudiante: 'Sofía Ramírez', fecha: '2026-09-04', perfil: 'Humanístico', recomendacion: 'Derecho', afinidad: '91%' }
  ]
})

const cerrarSesion = () => {
  router.push('/')
}
</script>

<template>
  <div class="panel-layout">
    <!-- Barra Lateral -->
    <aside class="sidebar">
      <div class="sidebar-header">
        <h3>Portal de Orientación</h3>
      </div>
      <nav class="sidebar-nav">
        <a href="#" class="active">Panel de Reportes</a>
        <a href="#">Estudiantes</a>
        <a href="#">Gestión de Preguntas</a>
        <a href="#">Estadísticas por Carrera</a>
      </nav>
      <div class="sidebar-footer">
        <button @click="cerrarSesion" class="btn-salir">Cerrar Sesión</button>
      </div>
    </aside>

    <!-- Contenido Principal -->
    <main class="main-content">
      <header class="top-bar">
        <h2>Reportes de Cuestionarios Vocacionales</h2>
        <div class="user-info">Administrador</div>
      </header>

      <div class="dashboard-widgets">
        <div class="widget-card">
          <h4>Cuestionarios Completados</h4>
          <p class="widget-number">128</p>
        </div>
        <div class="widget-card">
          <h4>Carrera Más Recomendada</h4>
          <p class="widget-text">Licenciatura en Sistemas</p>
        </div>
        <div class="widget-card">
          <h4>Precisión del Modelo AI</h4>
          <p class="widget-status online">Alta (92%)</p>
        </div>
      </div>

      <div class="table-container">
        <h3>Últimos Resultados Procesados</h3>
        <table class="data-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Estudiante</th>
              <th>Fecha</th>
              <th>Perfil Detectado</th>
              <th>Carrera Recomendada</th>
              <th>Nivel de Afinidad</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="reporte in reportesRecientes" :key="reporte.id">
              <td>#{{ reporte.id }}</td>
              <td><strong>{{ reporte.estudiante }}</strong></td>
              <td>{{ reporte.fecha }}</td>
              <td>{{ reporte.perfil }}</td>
              <td><span class="highlight">{{ reporte.recomendacion }}</span></td>
              <td>
                <span class="badge alta">{{ reporte.afinidad }}</span>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </main>
  </div>
</template>

<style scoped>
.panel-layout {
  display: flex;
  min-height: 100vh;
  background-color: #f4f8fc;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* Sidebar */
.sidebar {
  width: 260px;
  background-color: #2c3e50;
  color: white;
  display: flex;
  flex-direction: column;
}

.sidebar-header {
  padding: 20px;
  background-color: #1a252f;
  text-align: center;
}

.sidebar-nav {
  display: flex;
  flex-direction: column;
  padding: 20px 0;
  flex-grow: 1;
}

.sidebar-nav a {
  color: #bdc3c7;
  text-decoration: none;
  padding: 15px 25px;
  transition: all 0.2s;
}

.sidebar-nav a:hover, .sidebar-nav a.active {
  background-color: #34495e;
  color: #ffffff;
  border-left: 4px solid #3498db;
}

.sidebar-footer {
  padding: 20px;
}

.btn-salir {
  width: 100%;
  padding: 10px;
  background-color: transparent;
  color: #e74c3c;
  border: 1px solid #e74c3c;
  border-radius: 4px;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.2s;
}

.btn-salir:hover {
  background-color: #e74c3c;
  color: white;
}

/* Main Content */
.main-content {
  flex-grow: 1;
  display: flex;
  flex-direction: column;
}

.top-bar {
  background-color: white;
  padding: 20px 30px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 2px 5px rgba(0,0,0,0.05);
}

.top-bar h2 {
  margin: 0;
  color: #2c3e50;
  font-size: 1.3rem;
}

/* Widgets */
.dashboard-widgets {
  display: flex;
  gap: 20px;
  padding: 30px;
}

.widget-card {
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  flex: 1;
  box-shadow: 0 4px 6px rgba(0,0,0,0.05);
  text-align: center;
  border-top: 4px solid #3498db;
}

.widget-card h4 {
  margin: 0 0 10px 0;
  color: #7f8c8d;
  font-size: 0.9rem;
  text-transform: uppercase;
}

.widget-number, .widget-text {
  font-size: 1.8rem;
  font-weight: bold;
  color: #2c3e50;
  margin: 0;
}

.widget-text {
  font-size: 1.2rem;
  margin-top: 10px;
}

.widget-status {
  font-size: 1.2rem;
  font-weight: bold;
  margin: 0;
}

.widget-status.online { color: #27ae60; }

/* Table */
.table-container {
  background-color: white;
  margin: 0 30px 30px 30px;
  padding: 25px;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0,0,0,0.05);
}

.table-container h3 {
  margin-top: 0;
  color: #2c3e50;
  margin-bottom: 20px;
}

.data-table {
  width: 100%;
  border-collapse: collapse;
}

.data-table th, .data-table td {
  padding: 15px;
  text-align: left;
  border-bottom: 1px solid #ecf0f1;
}

.data-table th {
  background-color: #f8f9fa;
  color: #7f8c8d;
  font-weight: 600;
  text-transform: uppercase;
  font-size: 0.85rem;
}

.highlight {
  color: #3498db;
  font-weight: 600;
}

.badge {
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: bold;
}

.badge.alta {
  background-color: #d4edda;
  color: #155724;
}
</style>