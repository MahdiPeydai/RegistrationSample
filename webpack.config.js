const path = require('path');
const { WebpackManifestPlugin } = require('webpack-manifest-plugin');
const webpack = require('webpack');

module.exports = {
    entry: {
        layout : './src/js/layout.js',
        admin_panel : './src/js/admin_panel.js',
        edit_page : './src/js/edit_page.js',
        authentication : './src/js/authentication.js'
    },
    output: {
        path : path.resolve(__dirname, 'static'),
        filename : '[name].js',
        clean: true,
        assetModuleFilename: '[name][ext]',
    },
    plugins: [
        new WebpackManifestPlugin(),
        new webpack.ProvidePlugin({
            $: 'jquery',
            jQuery: 'jquery'
        })
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