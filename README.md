# Cyber Security News API

This is a Flask-based API that scrapes and provides the latest cybersecurity news. The API is deployed on **Vercel** for easy access.

---

## 🚀 Deployment Guide (Vercel)

### 1️⃣ **Install Vercel CLI**
If you haven't installed Vercel yet, install it using npm:
```bash
npm install -g vercel
```

### 2️⃣ **Set Up Your Project**
Ensure your project has the following structure:
```
📂 project-root/
 ├── 📂 api/          # Your API folder (must be named 'api')
 │   ├── index.py     # Your Flask API file (must be 'index.py')
 ├── requirements.txt # Your dependencies
 ├── vercel.json      # Your Vercel config
```

### 3️⃣ **Create `requirements.txt`**
List all required Python packages:
```bash
Flask
requests
beautifulsoup4
fake_useragent
```

### 4️⃣ **Create `vercel.json`**
This file tells Vercel how to deploy your Flask app:
```json
{
  "builds": [
    {
      "src": "api/index.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/api/(.*)",
      "dest": "api/index.py"
    }
  ],
  "buildCommand": "pip install -r requirements.txt"
}
```

### 5️⃣ **Run Locally for Testing**
To test locally, run:
```bash
vercel dev
```
Visit **http://localhost:3000/api/news** to check if it's working.

### 6️⃣ **Deploy to Vercel**
Deploy your API with:
```bash
vercel --prod
```
Once deployed, your API will be live at:
```
https://your-vercel-app.vercel.app/api/news
```

---

## 📝 **Available Endpoints**
| Method | Endpoint     | Description               |
|--------|-------------|---------------------------|
| GET    | `/api/news` | Fetch latest news        |

---

## 🏠 **Main Documentation Page**
The root (`/`) of your app will display API documentation in HTML.

---

### 🎯 **Troubleshooting**
If you encounter **404 errors**, ensure:
✅ `index.py` is inside `/api/`
✅ `vercel.json` is configured correctly
✅ `vercel --force` is used for redeployment

For logs, check:
```bash
vercel logs your-vercel-app --prod
```

---

### 📢 **Enjoy Your Deployed Flask API on Vercel! 🚀**

