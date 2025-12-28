# Prashant Singh - Personal Website

Personal website and technical blog built with Hugo and the PaperMod theme.

## About

Data Engineer @ Nomura with 11+ years of experience in FinTech, specializing in Risk Management and Data Engineering.

## Tech Stack

- **Framework**: [Hugo](https://gohugo.io/) - Fast static site generator
- **Theme**: [PaperMod](https://github.com/adityatelange/hugo-PaperMod)
- **Deployment**: Netlify
- **Domain**: singhprashant.in

## Local Development

### Prerequisites

- [Hugo Extended](https://gohugo.io/installation/) (v0.140.2 or later)

### Running Locally

```bash
# Clone the repository
git clone <your-repo-url>
cd singhprashant

# Start the development server
hugo server -D

# Build for production
hugo --gc --minify
```

The site will be available at `http://localhost:1313/`

## Project Structure

```
.
├── archetypes/       # Content templates
├── content/          # Blog posts and pages
│   └── posts/        # Blog posts
├── layouts/          # Custom layout overrides
│   └── partials/     # Partial templates
├── static/           # Static assets (images, etc.)
├── themes/           # Hugo themes
│   └── PaperMod/     # PaperMod theme
├── hugo.toml         # Site configuration
└── netlify.toml      # Netlify deployment config
```

## Creating New Posts

```bash
hugo new posts/my-new-post.md
```

## Deployment

This site is automatically deployed to Netlify on every push to the main branch.

### Manual Deployment

1. Build the site: `hugo --gc --minify`
2. Deploy the `public/` directory

## License

Content © 2025 Prashant Singh. All rights reserved.
