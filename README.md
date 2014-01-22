# Blackhole HTTP/HTTPS Proxy Server

This is a blackhole proxy server written in Python that kills any request and optionally serves a custom message instead of a website.

## Why would you need this?

This is an important piece of [Focus](http://www.heyfocus.com/), a Mac app that blocks distracting websites.

## How does it work?

Rather than implement a full HTTP proxy server, this just returns an HTTP response. For HTTPS it just drops the connection. You can install custom certificates to intercept SSL too (look up how Charles does this if you're interested).
