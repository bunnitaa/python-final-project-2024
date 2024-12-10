# Issue: Database Encryption

## Problem Description
- The database was storing sensitive information (tasks) in plain text.
- This posed a security risk.

## Root Cause Analysis
- Sensitive data was not encrypted before being stored.
- No encryption mechanism was implemented.

## Resolution
- Integrated the `cryptography` library to encrypt tasks before storing them.
- Added decryption logic to retrieve tasks securely.

## Prevention
- Ensure all sensitive data is encrypted.
- Regularly review code for potential security vulnerabilities.
