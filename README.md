# Deprecation Notice

🚨 **This repository is deprecated and no longer maintained.** 🚨

This project is no longer actively developed or maintained. We recommend using [allora-offchain-node](https://github.com/allora-network/allora-offchain-node) as a replacement.

## Why is this project deprecated?

The architecture has been improved and simplified, and heads and workers supported by this project are are not compatible. 


## What should you do?

- **Switch to allora-offchain-node**: [allora-offchain-node](https://github.com/allora-network/allora-offchain-node)
- **Read the Docs**: Refer to docs on architecture (and workers specifically) on [Allora Network Docs](https://docs.allora.network/).


Thank you to everyone who contributed to this project.




Allora Inference Extension
=====================================

![Go!](https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white)
![Apache License](https://img.shields.io/badge/Apache%20License-D22128?style=for-the-badge&logo=Apache&logoColor=white)

LATEST CID `bafybeigx43n7kho3gslauwtsenaxehki6ndjo3s63ahif3yc5pltno3pyq`


This document provides instructions on how to use the Makefile for building the extension.

Prerequisites
-------------

*   Go Programming Environment
*   GNU Make
*   Node.js and npm (for the `example` target)
*   Wget (for the `setup` target)

Makefile Targets
----------------

*   `build`: Compiles the Go source file into a binary.
*   `clean`: Removes the compiled binary and other generated files.
*   `example`: Runs a Node.js build script in the `allora-function-example` directory.
*   `setup`: Downloads and extracts the appropriate blockless runtime for the current OS and architecture.
*   `test`: Runs a test using the blockless runtime and the built wasm file.

Usage
-----

Run the following commands in your terminal:

*   To compile the source code:
    
        make build
    
*   To clean up generated files:
    
        make clean
    
*   To run the example Node.js project:
    
        make example
    
*   To set up the runtime environment:
    
        make setup
    
*   To run tests:
    
        make test
    

Notes
-----

The `setup` target automatically detects your operating system and CPU architecture to download the correct version of the blockless runtime. This process uses `wget` and `tar` for downloading and extracting the files, respectively.

The `test` target depends on both the `build` and `example` targets, ensuring that all necessary components are built before testing.

Support
-------

For support, ensure that you have all the prerequisites installed and that your environment is set up correctly. If you encounter any issues, check the console output for error messages that may provide more information.

In particular, you may need to install the blockless package:
```
 npm i -g @blockless/cli@<release-version>
```
