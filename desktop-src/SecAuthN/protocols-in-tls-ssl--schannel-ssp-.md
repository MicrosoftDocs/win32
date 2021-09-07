---
description: The schannel SSP implements versions of the TLS, DTLS and SSL protocols. Different Windows versions support different protocol versions.
ms.assetid: FF716A4E-ABF2-4773-9588-9D200945A866
title: Protocols in TLS/SSL (Schannel SSP)
ms.topic: article
ms.date: 01/20/2021
ms.custom: contperf-fy21q3
---

# Protocols in TLS/SSL (Schannel SSP)

The Schannel SSP implements versions of the TLS, DTLS and SSL protocols. Different Windows versions support different protocol versions.

## TLS protocol version support

The following table displays the Microsoft Schannel Provider support of TLS protocol versions.

> [!TIP]
> You may need to scroll horizontally to view all columns in the table.

| Windows OS | TLS 1.0 Client | TLS 1.0 Server | TLS 1.1 Client | TLS 1.1 Server | TLS 1.2 Client | TLS 1.2 Server | TLS 1.3 Client | TLS 1.3 Server |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| Windows Vista/Windows Server 2008                     | Enabled        | Enabled        | Not supported  | Not supported  | Not supported  | Not supported  | Not supported  | Not supported  |
| Windows Server 2008 with Service Pack 2 (SP2)         | Enabled        | Enabled        | Disabled       | Disabled       | Disabled       | Disabled       | Not supported  | Not supported  |
| Windows 7/Windows Server 2008 R2                      | Enabled        | Enabled        | Disabled       | Disabled       | Disabled       | Disabled       | Not supported  | Not supported  |
| Windows 8/Windows Server 2012                         | Enabled        | Enabled        | Enabled        | Enabled        | Enabled        | Enabled        | Not supported  | Not supported  |
| Windows 8.1/Windows Server 2012 R2                    | Enabled        | Enabled        | Enabled        | Enabled        | Enabled        | Enabled        | Not supported  | Not supported  |
| Windows 10, version 1507                              | Enabled        | Enabled        | Enabled        | Enabled        | Enabled        | Enabled        | Not supported  | Not supported  |
| Windows 10, version 1511                              | Enabled        | Enabled        | Enabled        | Enabled        | Enabled        | Enabled        | Not supported  | Not supported  |
| Windows 10, version 1607/Windows Server 2016 Standard | Enabled        | Enabled        | Enabled        | Enabled        | Enabled        | Enabled        | Not supported  | Not supported  |
| Windows 10, version 1703                              | Enabled        | Enabled        | Enabled        | Enabled        | Enabled        | Enabled        | Not supported  | Not supported  |
| Windows 10, version 1709                              | Enabled        | Enabled        | Enabled        | Enabled        | Enabled        | Enabled        | Not supported  | Not supported  |
| Windows 10, version 1803                              | Enabled        | Enabled        | Enabled        | Enabled        | Enabled        | Enabled        | Not supported  | Not supported  |
| Windows 10, version 1809//Windows Server 2019         | Enabled        | Enabled        | Enabled        | Enabled        | Enabled        | Enabled        | Not supported  | Not supported  |
| Windows 10, version 1903                              | Enabled        | Enabled        | Enabled        | Enabled        | Enabled        | Enabled        | Not supported  | Not supported  |
| Windows 10, version 1909                              | Enabled        | Enabled        | Enabled        | Enabled        | Enabled        | Enabled        | Not supported  | Not supported  |
| Windows 10, version 2004                              | Enabled        | Enabled        | Enabled        | Enabled        | Enabled        | Enabled        | Not supported  | Not supported  |
| Windows 10, version 20H2                              | Enabled        | Enabled        | Enabled        | Enabled        | Enabled        | Enabled        | Not supported  | Not supported  |
| Windows 10, version 21H1                              | Enabled        | Enabled        | Enabled        | Enabled        | Enabled        | Enabled        | Not supported  | Not supported  |
| Windows Server 2022                                   | Enabled        | Enabled        | Enabled        | Enabled        | Enabled        | Enabled        | Enabled        | Enabled        |
| Windows 11                                            | Enabled        | Enabled        | Enabled        | Enabled        | Enabled        | Enabled        | Enabled        | Enabled        |

## DTLS protocol version support

The following lists the Microsoft Schannel Provider support of DTLS protocol versions.

*Tip: you may need to scroll horizontally to view all columns in this table:*

| Windows OS                                            | DTLS 1.0 Client | DTLS 1.0 Server | DTLS 1.2 Client | DTLS 1.2 Server |
|-------------------------------------------------------|-----------------|-----------------|-----------------|-----------------|
| Windows Vista/Windows Server 2008                     | Not supported   | Not supported   | Not supported   | Not supported   |
| Windows Server 2008 with SP2                          | Not supported   | Not supported   | Not supported   | Not supported   |
| Windows 7/Windows Server 2008 R2                      | Enabled         | Enabled         | Not supported   | Not supported   |
| Windows 8/Windows Server 2012                         | Enabled         | Enabled         | Not supported   | Not supported   |
| Windows 8.1/Windows Server 2012 R2                    | Enabled         | Enabled         | Not supported   | Not supported   |
| Windows 10, version 1507                              | Enabled         | Enabled         | Not supported   | Not supported   |
| Windows 10, version 1511                              | Enabled         | Enabled         | Not supported   | Not supported   |
| Windows 10, version 1607/Windows Server 2016 Standard | Enabled         | Enabled         | Enabled         | Enabled         |
| Windows 10, version 1703                              | Enabled         | Enabled         | Enabled         | Enabled         |
| Windows 10, version 1803                              | Enabled         | Enabled         | Enabled         | Enabled         |
| Windows 10, version 1809                              | Enabled         | Enabled         | Enabled         | Enabled         |
| Windows 10, version 1903                              | Enabled         | Enabled         | Enabled         | Enabled         |
| Windows 10, version 1909                              | Enabled         | Enabled         | Enabled         | Enabled         |
| Windows 10, version 2004                              | Enabled         | Enabled         | Enabled         | Enabled         |
| Windows 10, version 20H2                              | Enabled         | Enabled         | Enabled         | Enabled         |
| Windows 10, version 21H1                              | Enabled         | Enabled         | Enabled         | Enabled         |
| Windows Server 2022                                   | Enabled         | Enabled         | Enabled         | Enabled         |
| Windows 11                                            | Enabled         | Enabled         | Enabled         | Enabled         |

## Pre-TLS standard protocols support

The following lists the Microsoft Schannel Provider support of pre-TLS standard protocols:

*Tip: you may need to scroll horizontally to view all columns in this table:*

| Windows OS                                            | PCT 1.0       | SSL2 Client   | SSL2 Server   | SSL3 Client | SSL3 Server |
|-------------------------------------------------------|---------------|---------------|---------------|-------------|-------------|
| Windows Vista/Windows Server 2008                     | Not supported | Disabled      | Enabled       | Enabled     | Enabled     |
| Windows Server 2008 with SP2                          | Not supported | Disabled      | Enabled       | Enabled     | Enabled     |
| Windows 7/Windows Server 2008 R2                      | Not supported | Disabled      | Enabled       | Enabled     | Enabled     |
| Windows 8/Windows Server 2012                         | Not supported | Disabled      | Disabled      | Enabled     | Enabled     |
| Windows 8.1/Windows Server 2012 R2                    | Not supported | Disabled      | Disabled      | Enabled     | Enabled     |
| Windows 10, version 1507                              | Not supported | Disabled      | Disabled      | Enabled     | Enabled     |
| Windows 10, version 1511                              | Not supported | Disabled      | Disabled      | Enabled     | Enabled     |
| Windows 10, version 1607/Windows Server 2016 Standard | Not supported | Not supported | Not supported | Disabled    | Disabled    |
| Windows 10, version 1703                              | Not supported | Not supported | Not supported | Disabled    | Disabled    |
| Windows 10, version 1803                              | Not supported | Not supported | Not supported | Disabled    | Disabled    |
| Windows 10, version 1809                              | Not supported | Not supported | Not supported | Disabled    | Disabled    |
| Windows 10, version 1903                              | Not supported | Not supported | Not supported | Disabled    | Disabled    |
| Windows 10, version 1909                              | Not supported | Not supported | Not supported | Disabled    | Disabled    |
| Windows 10, version 2004                              | Not supported | Not supported | Not supported | Disabled    | Disabled    |
| Windows 10, version 20H2                              | Not supported | Not supported | Not supported | Disabled    | Disabled    |
| Windows 10, version 21H1                              | Not supported | Not supported | Not supported | Disabled    | Disabled    |
| Windows Server 2022                                   | Not supported | Not supported | Not supported | Disabled    | Disabled    |
| Windows 11                                            | Not supported | Not supported | Not supported | Disabled    | Disabled    |

> [!IMPORTANT]
> Beginning with Windows 10, version 1607 and Windows Server 2016, SSL 2.0 has been removed and is no longer supported.

> [!TIP]  
> All versions of Windows will accept a unified format "ClientHello" message even when SSL version 2 is disabled or no longer supported.
