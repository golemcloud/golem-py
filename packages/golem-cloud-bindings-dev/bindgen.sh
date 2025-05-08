#! /bin/sh

rm -rf src/golem_cloud_bindings/bindings
componentize-py --import-interface-name "wasi:http/types@0.2.0"="types" --import-interface-name "wasi:http/outgoing-handler@0.2.0"="outgoing_handler" --wit-path wit bindings --world-module bindings src/golem_cloud_bindings
