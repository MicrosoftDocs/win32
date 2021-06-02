---
description: Communication often involves potentially large amounts of data or data of unknown length.
ms.assetid: e7b12b9e-8caa-4dad-b81f-b609ccb92c9f
title: Using SecBufferDesc and SecBuffer
ms.topic: article
ms.date: 05/31/2018
---

# Using SecBufferDesc and SecBuffer

Communication often involves potentially large amounts of data or data of unknown length. Sending and receiving data is done in similar or identical fashion in both of these cases. To deal with unknown length and potentially large amounts of data, SSPI communication is done using two structures, [**SecBufferDesc**](/windows/desktop/api/Sspi/ns-sspi-secbufferdesc) and [**SecBuffer**](/windows/desktop/api/Sspi/ns-sspi-secbuffer).

A [**SecBufferDesc**](/windows/desktop/api/Sspi/ns-sspi-secbufferdesc) structure is a container for an array of [**SecBuffer**](/windows/desktop/api/Sspi/ns-sspi-secbuffer) structures. A **SecBufferDesc** structure has the following members:

-   Version number
-   Number of [**SecBuffer**](/windows/desktop/api/Sspi/ns-sspi-secbuffer) elements
-   Address of the array of [**SecBuffer**](/windows/desktop/api/Sspi/ns-sspi-secbuffer) structures

A [**SecBuffer**](/windows/desktop/api/Sspi/ns-sspi-secbuffer) structure contains the following three members:

-   Number of bytes in the buffer
-   Type of information contained in the data item
-   The bytes themselves

A whole SSPI message often consists of an array of [**SecBuffer**](/windows/desktop/api/Sspi/ns-sspi-secbuffer) structures.

The following buffer data types are defined as follows.



| Buffer type                | Meaning                                                                                                                                |
|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| SECBUFFER\_EMPTY           | Undefined, replaced by the [*security package*](../secgloss/s-gly.md) function |
| SECBUFFER\_DATA            | Packet data                                                                                                                            |
| SECBUFFER\_TOKEN           | Security token                                                                                                                         |
| SECBUFFER\_PKG\_PARAMS     | Package-specific parameters                                                                                                            |
| SECBUFFER\_MISSING         | Missing data indicator                                                                                                                 |
| SECBUFFER\_EXTRA           | Extra data                                                                                                                             |
| SECBUFFER\_STREAM          | Security stream data                                                                                                                   |
| SECBUFFER\_STREAM\_TRAILER | Security stream trailer                                                                                                                |
| SECBUFFER\_STREAM\_HEADER  | Security stream header                                                                                                                 |



 

The buffer types above can be combined using a bitwise-**OR** operation with either of the following buffer types.



| Buffer type         | Meaning                                                                          |
|---------------------|----------------------------------------------------------------------------------|
| SECBUFFER\_ATTRMASK | Mask security attributes by separating the attribute flags from the buffer type. |
| SECBUFFER\_READONLY | Buffer is read-only                                                              |



 

Before each call to an SSPI API that requires a [**SecBufferDesc**](/windows/desktop/api/Sspi/ns-sspi-secbufferdesc) parameter, one or more [**SecBuffer**](/windows/desktop/api/Sspi/ns-sspi-secbuffer) array elements are declared and initialized. For example, there can be two security buffers: one that contains input message data and the other for the output opaque security token returned by the security package. The order of security buffers in the security buffer descriptor is not important, but each buffer must be tagged with its appropriate type. A read-only tag can be used with any input buffer that must not be modified by the [*security package*](../secgloss/s-gly.md).

The size of the output buffer that is expected to contain the security token is important. An application can find the maximum token size for a security package during initial setup. The call to [**EnumerateSecurityPackages**](/windows/desktop/api/Sspi/nf-sspi-enumeratesecuritypackagesa) returns an array of pointers to security package information. The security package information structure contains the maximum token size for each package. In the example, the information is in the **cbMaxToken** member of the [**SecPkgInfo**](/windows/desktop/api/Sspi/ns-sspi-secpkginfoa) structure. The same information can be obtained later using [**QuerySecurityPackageInfo**](/windows/desktop/api/Sspi/nf-sspi-querysecuritypackageinfoa).

The application initializes the buffer pointers and sizes in the buffer description to indicate where message data and other information can be found.

For details, see [SecBuffer and SecBufferDesc Example Code](secbuffer-and-secbufferdesc-example-code.md).

 

 
