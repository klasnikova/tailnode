const path = require('path');

module.exports = {
    entry: {
        'tailnode-site':'./src/styles/tailnode-site.css',
        'tailnode-addons':'./src/styles/tailnode-addons.css',
        'tailnode-htmx':'./src/scripts/tailnode-htmx.js'
    },
    output: {
        path: path.resolve(__dirname, 'static', 'assets', 'bundles'),
        filename: '[name].bundle.js',
    },
    module: {
        rules: [
            {
                test: /\.css$/,
                use: ['style-loader', 'css-loader', 'postcss-loader'],
            },
        ],
    },
};
