# Calculator Website

A simple, responsive calculator web application ready to deploy on cloud services.

## Features

- ✨ Clean and modern UI with gradient background
- 🔢 Basic arithmetic operations (addition, subtraction, multiplication, division)
- ⌨️ Keyboard support for faster input
- 📱 Fully responsive design (works on mobile and desktop)
- 🚀 Ready for cloud deployment

## Files

- `index.html` - Main HTML structure
- `styles.css` - Styling and responsive design
- `script.js` - Calculator logic and keyboard functionality
- `package.json` - Project metadata

## Usage

1. Open `index.html` in any web browser
2. Click buttons or use your keyboard:
   - Numbers: `0-9`
   - Operations: `+ - * /`
   - Decimal: `.`
   - Calculate: `Enter`
   - Clear: `Escape`
   - Delete last: `Backspace`

## Local Development

```bash
# Option 1: Using Python (built-in)
python -m http.server 8000

# Option 2: Using Node.js http-server
npm install -g http-server
http-server -p 8000

# Option 3: Using Live Server extension in VS Code
# Install "Live Server" extension and click "Go Live"
```

Then open `http://localhost:8000` in your browser.

## Cloud Deployment Options

### 1. **Netlify (Recommended - Free & Easy)**
```bash
npm install -g netlify-cli
netlify deploy --prod --dir .
```

### 2. **Vercel**
```bash
npm install -g vercel
vercel
```

### 3. **GitHub Pages**
1. Push files to GitHub repository
2. Go to Settings → Pages
3. Select main branch as source

### 4. **AWS S3 + CloudFront**
```bash
aws s3 cp . s3://your-bucket/ --recursive
```

### 5. **Azure Static Web Apps**
- Connect your GitHub repo to Azure Static Web Apps

### 6. **Firebase Hosting**
```bash
npm install -g firebase-tools
firebase init hosting
firebase deploy
```

### 7. **Heroku** (Node.js server needed)
Create `server.js`:
```javascript
const express = require('express');
const app = express();
app.use(express.static('.'));
const PORT = process.env.PORT || 8000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

Then deploy:
```bash
heroku create
git push heroku main
```

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers

## License

MIT License - Free to use for personal and commercial projects

## Author

Created as a sample calculator project for learning and deployment purposes.
