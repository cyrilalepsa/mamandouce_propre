const WebpackHealthPlugin = require('./scripts/webpack-health-plugin');
const setupHealthEndpoints = require('./scripts/health-endpoints');

const healthPlugin = new WebpackHealthPlugin();

module.exports = {
  // ... tes réglages habituels ...
  plugins: [
    healthPlugin, // Le plugin surveille
    // ...
  ],
  devServer: {
    onBeforeSetupMiddleware: (devServer) => {
      setupHealthEndpoints(devServer, healthPlugin); // Les endpoints diffusent
    }
  }
};