---
description: Stream contexts handle the secure stream-oriented protocols such as SSL or PCT.
ms.assetid: 05a6b036-1f7f-473f-9813-a1e1534e0f0d
title: Stream Contexts
ms.topic: article
ms.date: 05/31/2018
---

# Stream Contexts

Stream contexts handle the secure stream-oriented protocols such as SSL or PCT. In the interest of sharing the same interface and similar credential management, SSPI provides support for stream contexts. The [*security protocol*](../secgloss/s-gly.md) incorporates both the stream authentication scheme and record formats.

To provide stream-oriented protocols, [*security packages*](../secgloss/s-gly.md) that support stream contexts have the following process characteristics:

-   The package sets the SECPKG\_FLAG\_STREAM flag to indicate that it supports stream semantics.
-   Transport applications requests stream semantics by setting the ISC\_REQ\_STREAM and ASC\_REQ\_STREAM flags in the calls to the [**InitializeSecurityContext (General)**](/windows/win32/api/sspi/nf-sspi-initializesecuritycontexta) and [**AcceptSecurityContext (General)**](/windows/win32/api/sspi/nf-sspi-acceptsecuritycontext) functions.
-   The application calls the [**QueryContextAttributes (General)**](/windows/win32/api/sspi/nf-sspi-querycontextattributesa) function with a [**SecPkgContext\_StreamSizes**](/windows/desktop/api/Sspi/ns-sspi-secpkgcontext_streamsizes) structure to query the [*security context*](../secgloss/s-gly.md) for the number of buffers to provide and the sizes to reserve for headers or trailers.
-   The application provides buffer descriptors to spare during the actual processing of the data. By specifying stream semantics, the caller indicates willingness to do extra processing so that the [*security package*](../secgloss/s-gly.md) can handle the blocking of the messages. In essence, for the [**MakeSignature**](/windows/desktop/api/Sspi/nf-sspi-makesignature) and [**VerifySignature**](/windows/desktop/api/Sspi/nf-sspi-verifysignature) functions, the caller passes in a list of buffers. When a message is received from a channel that is stream-oriented (such as a TCP port), the caller passes in a buffer list as follows.

    | Buffer | Length         | Buffer type      |
    |--------|----------------|------------------|
    | 1      | Message Length | SECBUFFER\_DATA  |
    | 2      | 0              | SECBUFFER\_EMPTY |
    | 3      | 0              | SECBUFFER\_EMPTY |
    | 4      | 0              | SECBUFFER\_EMPTY |
    | 5      | 0              | SECBUFFER\_EMPTY |

    

     

    The security package then works on the [*BLOB*](../secgloss/b-gly.md). If the function returns successfully, the buffer list looks like the following.

    

    | Buffer | Length         | Buffer type                |
    |--------|----------------|----------------------------|
    | 1      | Header Length  | SECBUFFER\_STREAM\_HEADER  |
    | 2      | Data Length    | SECBUFFER\_DATA            |
    | 3      | Trailer Length | SECBUFFER\_STREAM\_TRAILER |
    | 4      | 0              | SECBUFFER\_EMPTY           |
    | 5      | 0              | SECBUFFER\_EMPTY           |

    

     

    The package could have also returned buffer \#4 with length x and buffer type SECBUFFER\_EXTRA indicating that the data in this buffer is part of the next record and has not yet been processed. Conversely, if the message function returns the SEC\_E\_INCOMPLETE\_MESSAGE error code, the returned buffer list would look like the following.

    

    | Buffer | Length | Buffer type        |
    |--------|--------|--------------------|
    | 1      | x      | SECBUFFER\_MISSING |

    

     

    This indicates that more data was needed to process the record. Unlike most errors returned from a message function, this buffer type does not indicate that the context has been compromised. Instead, it indicates that more data is needed. [*security packages*](../secgloss/s-gly.md) must not update their [*state*](../secgloss/s-gly.md) in this condition.

    Similarly, on the sender side of the communication, the caller can call the [**MakeSignature**](/windows/desktop/api/Sspi/nf-sspi-makesignature) function. The security package may need to reallocate the buffer or copy things around. The caller can be more efficient by providing a buffer list as follows.

    

    | Buffer | Length         | Type                       |
    |--------|----------------|----------------------------|
    | 1      | Header Length  | SECBUFFER\_STREAM\_HEADER  |
    | 2      | Data Length    | SECBUFFER\_DATA            |
    | 3      | Trailer Length | SECBUFFER\_STREAM\_TRAILER |

    

     

    This allows the caller to use the buffers more efficiently. By calling the [**QueryContextAttributes**](/windows/win32/api/sspi/nf-sspi-querycontextattributesa) function to determine the amount of space to reserve before calling [**MakeSignature**](/windows/desktop/api/Sspi/nf-sspi-makesignature), the operation is more efficient for the application and the security package.

 

 
