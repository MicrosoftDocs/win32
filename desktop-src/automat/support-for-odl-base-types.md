---
title: Support for ODL Base Types
description: There are a number of ODL base types that are not directly supported by MIDL.
ms.assetid: 'c8e6efe1-8e39-47bc-9ba2-5dac91264666'
---

# Support for ODL Base Types

There are a number of ODL base types that are not directly supported by MIDL. The MIDL function gets its definitions for these base types by automatically importing oaidl.idl, and oleidl.idl whenever it encounters a library statement. This means that oaidl.idl, and oleidl.idl (along with the imported unknwn.idl and wtypes.idl files) must be somewhere in the user's INCLUDE path. The OLE and Automation DLLs must also be in the system if the user compiles an .idl file that contains a library statement.

 

 




