# React Challenges Setup Guide

This guide will help you set up and run the React challenges.

## Prerequisites
- Node.js (v14 or higher)
- npm (v6 or higher)

## Setup Instructions

### For each challenge (counter-app and data-grid):

1. Navigate to the challenge directory:
```bash
cd counter-app
# or
cd data-grid
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```

The app will open in your default browser at `http://localhost:3000`.

## Project Structure

Each challenge follows this structure:
```
src/
  ├── components/          # Challenge components
  │   └── [Component]/
  │       ├── Component.shell.tsx    # Component shell to implement
  │       ├── types.shell.ts         # TypeScript types
  │       └── Component.test.tsx     # Test file
  ├── App.tsx             # Main app component
  └── index.tsx          # Entry point
```

## Testing

Run the tests:
```bash
npm test
```

## Building

Create a production build:
```bash
npm run build
```

## Notes
- The shell files contain the basic structure and types you need to implement
- Tests are provided to help guide your implementation
- Feel free to add additional helper components or utilities as needed
- Make sure all tests pass before submitting your solution
