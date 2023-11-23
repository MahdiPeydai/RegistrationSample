const path = require('path');
const { WebpackManifestPlugin } = require('webpack-manifest-plugin');

module.exports = {
    entry: {
        layout : './src/js/layout.js',
    },
    output: {
        path : path.resolve(__dirname, 'static'),
        filename : '[name].js',
        clean: true,
        assetModuleFilename: '[name][ext]',
    },
    plugins: [
        new WebpackManifestPlugin()
    ],
    module: {
        rules: [
            {
                test: /\.css$/i,
                use: ['style-loader', 'css-loader']
            },
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['@babel/preset-env'],
                    },
                },
            },
        ]
    }
}