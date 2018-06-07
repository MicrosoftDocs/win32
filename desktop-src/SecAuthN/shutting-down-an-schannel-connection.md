---
Description: Shutting Down an Schannel Connection
ms.assetid: 7081ba1f-df3c-41b4-96da-24d44e74d714
title: Shutting Down an Schannel Connection
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Shutting Down an Schannel Connection

When a client or server is finished with a connection, it must shut it down. The other party, in turn, must recognize the shutdown and delete the connection.

**To shut down an Schannel connection**

1.  Call the [**ApplyControlToken**](/windows/desktop/api/Sspi/nf-sspi-applycontroltoken) function, specifying the SCHANNEL\_SHUTDOWN control token.
2.  After receiving an SEC\_E\_OK return value from [**ApplyControlToken**](/windows/desktop/api/Sspi/nf-sspi-applycontroltoken), call the [**InitializeSecurityContext (Schannel)**](/windows/desktop/api/Sspi/) (clients) or [**AcceptSecurityContext (Schannel)**](/windows/desktop/api/Sspi/) (servers) function, passing in empty buffers.
3.  Proceed as though your application were creating a new connection until the function returns SEC\_I\_CONTEXT\_EXPIRED or SEC\_E\_OK to indicate that the connection is shut down.
4.  Send the final output information, if any, to the remote party.
5.  Call [**DeleteSecurityContext**](/windows/desktop/api/Sspi/nf-sspi-deletesecuritycontext) to free resources held by the connection.

## Recognizing a Shutdown

The [**DecryptMessage (Schannel)**](/windows/desktop/api/Sspi/) function returns SEC\_I\_CONTEXT\_EXPIRED when the message sender has shut down the connection. After receiving this return value, follow the procedure To shut down an Schannel connection, earlier in this topic.

 

 



