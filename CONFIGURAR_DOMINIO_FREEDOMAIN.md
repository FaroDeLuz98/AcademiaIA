# 🌐 Guía para Vincular tu Dominio Gratuito de FreeDomain con Academia IA

Esta guía te explica paso a paso cómo registrar tu dominio gratuito en **DigitalPlat FreeDomain** y conectarlo con **Academia IA** para acceder a tu plataforma desde cualquier lugar o compartirla.

---

## 1. Extensiones de Dominio Disponibles en FreeDomain

En **DigitalPlat FreeDomain** podés registrar gratis cualquiera de estas extensiones:
- `tu-academia.dpdns.org`
- `tu-academia.us.kg`
- `tu-academia.qzz.io`
- `tu-academia.xx.kg`
- `tu-academia.qd.je`

---

## 2. Paso a Paso: Registrar tu Dominio en FreeDomain

1. **Ingresá al panel de FreeDomain**:
   Abre [https://dash.domain.digitalplat.org/](https://dash.domain.digitalplat.org/) en tu navegador.
2. **Creá tu cuenta gratuita** (o inicia sesión si ya tenés una).
3. **Buscar y Registrar Dominio**:
   - Anda a la sección **Register Domain**.
   - Escribe el nombre que deseas (ejemplo: `miacademiaia`).
   - Elige una de las extensiones gratuitas (ej. `.dpdns.org` o `.us.kg`).
   - Haz clic en **Check availability** y confirma el registro.

---

## 3. Conectar los Nameservers (DNS) con Cloudflare (Recomendado por FreeDomain)

Tal como detalla el manual de FreeDomain (`FreeDomain-main/documents/tutorial/platform/1.3-connect-nameservers.md`):

1. Regístrate en [Cloudflare](https://dash.cloudflare.com/) (es 100% gratis).
2. Haz clic en **Add a site** e ingresa tu dominio registrado (ej. `miacademiaia.dpdns.org`).
3. Selecciona el **Plan Gratuito ($0)**.
4. Cloudflare te asignará dos Nameservers (ejemplo: `ns1.cloudflare.com` y `ns2.cloudflare.com`).
5. Vuelve al panel de **DigitalPlat FreeDomain**, entra a la configuración de tu dominio y pega esos dos Nameservers en **Custom Nameservers**.

---

## 4. Métodos para Desplegar Academia IA con tu Dominio

Tienes **dos opciones excelentes**:

### Opción A (Recomendada: 100% Online y Gratis 24/7 sin dejar tu PC prendida)
Dado que Academia IA es una aplicación web rápida y moderna (HTML5, JS y CSS con guardado local persistente):
1. Entra a **Cloudflare Dashboard** > **Workers & Pages** > **Pages**.
2. Haz clic en **Upload assets** y arrastra la carpeta `academia_dinero_v2` (o los archivos de `Academia IA`).
3. Asigna un nombre al proyecto (ej. `academia-ia`). ¡Listo, ya está online!
4. En la pestaña **Custom domains** de tu proyecto Pages, escribe tu dominio de FreeDomain (ej. `miacademiaia.dpdns.org`).
5. ¡Cloudflare le asigna automáticamente certificado SSL HTTPS gratis y tu dominio queda funcionando en todo el mundo!

### Opción B (Túnel directo desde tu PC a tu Dominio)
Si deseas que tu PC sirva la aplicación directamente a través de tu dominio:
1. Inicia Academia IA con `INICIAR_ACADEMIA.bat` (servidor en puerto 8000).
2. Usa **Cloudflare Tunnel** (`cloudflared`) o **localtunnel**:
   - Con Cloudflare Tunnel:
     ```cmd
     cloudflared tunnel --url http://localhost:8000
     ```
   - O usando Node.js / npx:
     ```cmd
     npx localtunnel --port 8000 --subdomain miacademiaia
     ```
3. En Cloudflare DNS de tu dominio FreeDomain, agrega un registro `CNAME` que apunte al túnel generado.

---

## 5. Script Automático

Hemos creado el script **`VINCULAR_FREEDOMAIN.bat`** en la carpeta principal que te ayuda a levantar el túnel público automáticamente hacia el puerto 8000.
