# quarterpie-site

SvelteKit site configured for Firebase App Hosting.

## Requirements

- Node.js 20+
- Yarn 1.x
- Firebase CLI access (`firebase login`)

## Local development

Install dependencies:

```sh
yarn
```

Start dev server:

```sh
yarn dev
```

## Production build (Firebase runtime parity)

Build:

```sh
yarn build
```

Run the production server locally:

```sh
yarn start
```

Or one-shot build + run:

```sh
yarn preview
```

## Firebase App Hosting setup

One-time initialization in this repo:

```sh
yarn firebase:init
```

That command connects this directory to your Firebase project/backend and updates Firebase metadata files as needed.

## Deploy

```sh
yarn deploy
```

If this is your first deploy from this machine, run:

```sh
firebase login
```
