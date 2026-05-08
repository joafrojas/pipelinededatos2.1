## Estructura del proyecto
pipeline_ingesta/
├── data/raw/ -> datos originales copiados
├── scripts/ -> scripts del pipeline
├── logs/ -> registros de ejecucion
└── README.md



# 1. ¿Qué es un Pipeline de Datos?

Un pipeline de datos es un proceso automatizado que permite mover, limpiar, transformar y almacenar datos de manera eficiente. Piensa en él como una línea de producción: cada etapa asegura que la información llegue lista, confiable y lista para ser analizada.

# 2. Ejemplo de uso en la industria

Empresas como Netflix usan pipelines de datos para procesar millones de eventos diarios, como qué series ven sus usuarios y cómo interactúan con el contenido. Esto les permite personalizar recomendaciones, mejorar la experiencia del usuario y tomar decisiones basadas en datos reales.

# 3. Riesgos de saltarse alguna etapa

Si se omite un paso del pipeline, pueden ocurrir problemas serios:

Datos incompletos, duplicados o erróneos.
Información incompatible con los sistemas de análisis.
Retrasos o errores en la toma de decisiones.

Cada etapa es fundamental para que los datos sean precisos y confiables, y saltarse alguna puede afectar directamente la calidad de la información y las decisiones de la empresa.
