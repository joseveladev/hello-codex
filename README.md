# hello-codex

Mini proyecto de demostracion creado y gestionado de forma automatizada por Codex.

## Que hace

Este repositorio contiene un `Hello World` en Python que imprime:

```text
Hola, soy Codex
```

Objetivo: validar un flujo completo de trabajo asistido por agente, desde la creacion del codigo hasta el versionado y publicacion en GitHub.

## Estructura del proyecto

```text
hello-codex/
├── main.py
├── README.md
└── .gitignore
```

- `main.py`: script principal.
- `README.md`: documentacion del proyecto.
- `.gitignore`: exclusion de secretos y archivos locales.

## Como ejecutarlo

Requisitos:
- Python 3 instalado.

Comando:

```bash
python3 main.py
```

## Lo que se hizo en este repositorio

1. Inicializacion del repositorio Git local.
2. Creacion del script base `main.py`.
3. Primer commit con el hello world.
4. Publicacion en GitHub (`main` como rama principal).
5. Endurecimiento basico de seguridad con `.gitignore`.

## Seguridad y buenas practicas

Este repo ignora por defecto:
- `.github_token`
- `.env` y `.env.*`
- cache de Python (`__pycache__/`, `*.pyc`)

Nunca se deben commitear tokens ni credenciales.

## Flujo de trabajo recomendado

Para cambios futuros:

```bash
git add .
git commit -m "feat: describe tu cambio"
git push
```

Formato de commits: Conventional Commits (`feat:`, `fix:`, `docs:`, `chore:`).
