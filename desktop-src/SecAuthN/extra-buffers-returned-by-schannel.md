---
description: Schannel has a well-defined set of behaviors for incomplete or excess information included in the input buffers to these functions.
ms.assetid: 5fad1e76-6520-4ff7-b2b0-2cc2061062a1
title: Extra Buffers Returned by Schannel
ms.topic: article
ms.date: 05/31/2018
---

# Extra Buffers Returned by Schannel

Information must be sent between the client and server while a [*security context*](/windows/desktop/SecGloss/s-gly) is being established and afterward because secure messages are exchanged by using the encryption and decryption features provided by Schannel. The following functions are used to accomplish these tasks:

-   [**AcceptSecurityContext (General)**](/windows/win32/api/sspi/nf-sspi-acceptsecuritycontext)
-   [**InitializeSecurityContext (General)**](/windows/win32/api/sspi/nf-sspi-initializesecuritycontexta)
-   [**DecryptMessage (General)**](/windows/win32/api/sspi/nf-sspi-decryptmessage)

Schannel has a well-defined set of behaviors for incomplete or excess information included in the input buffers to these functions. Information is exchanged between the client and server in the following manner:

1.  The local party interacts with Schannel by calling an SSPI function and passing in information. Typically, the information was received from the remote party.
2.  The function returns a status code and output buffers containing information.
3.  Depending on the status code, the output buffers are sent to the remote party by means of some communication mechanism.
4.  The remote party reads information sent by the local party.
5.  The loop repeats, with the local and remote parties interchanged. (The remote party calls an SSPI function and passes in the information read in the previous step.)

Everything works as expected when the input buffer to the SSPI function contains exactly the information needed. However, due to the stream-oriented nature of some communications protocols this may not be the case; a block of information received from a remote party may contain less data than is required or more data than can be processed by Schannel in a single function call.

If the input buffer contains too little information, the functions return SEC\_E\_INCOMPLETE\_MESSAGE. The caller must obtain additional data from the remote party and call the function again.

When the input buffers contains too much information, Schannel does not treat this as an error. The function processes as much of the input as it can, and returns the status code for that processing activity. In addition, Schannel indicates the presence of unprocessed information in the input buffers by returning an output buffer of type SECBUFFER\_EXTRA. Testing the output buffers for this type of buffer is the only way to detect this situation. The **cbBuffer** field of the extra buffer structure indicates how many bytes of input were not processed.

> [!Note]  
> The **pvBuffer** field of the extra buffer does not contain a copy of the excess data.

 

If you receive an extra buffer from a SSPI function, you must remove the already processed information from the input buffer and call the function again. Schannel can, and often does, return only the extra buffer and nothing else in the output buffers.

 

 
