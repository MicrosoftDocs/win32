---
title: Incremental Serialization
description: When using the incremental style serialization, you supply three routines to manipulate the buffer.
ms.assetid: c7383b4d-94d1-4edd-ac29-c11fb5343156
ms.topic: article
ms.date: 05/31/2018
---

# Incremental Serialization

When using the incremental style serialization, you supply three routines to manipulate the buffer. These routines are: Alloc, Read, and Write. The Alloc routine allocates a buffer of the required size. The Write routine writes the data into the buffer, and the Read routine retrieves a buffer that contains marshaled data. A single serialization call can make several calls to these routines.

The incremental style of serialization uses the following routines:

-   [**MesEncodeIncrementalHandleCreate**](/windows/desktop/api/Midles/nf-midles-mesencodeincrementalhandlecreate)
-   [**MesDecodeIncrementalHandleCreate**](/windows/desktop/api/Midles/nf-midles-mesdecodeincrementalhandlecreate)
-   [**MesIncrementalHandleReset**](/windows/desktop/api/Midles/nf-midles-mesincrementalhandlereset)
-   [**MesHandleFree**](/windows/desktop/api/Midles/nf-midles-meshandlefree)

The prototypes for the Alloc, Read, and Write functions that you must provide are shown below:

``` syntax
void __RPC_USER Alloc (
   void *State,          /* application-defined pointer */
   char **pBuffer,       /* returns pointer to allocated buffer */
   unsigned int *pSize); /* inputs requested bytes; outputs 
                         /* pBuffer size */

void __RPC_USER Write (
   void *State,          /* application-defined pointer */
   char *Buffer,         /* buffer with serialized data */
   unsigned int Size);   /* number of bytes to write from Buffer */

void __RPC_USER Read (
   void *State,          /* application-defined pointer */
   char **pBuffer,       /* returned pointer to buffer with data */
   unsigned int *pSize); /* number of bytes to read into pBuffer */
```

The State input a parameter for all three functions is the application-defined pointer that was associated with the encoding services handle. The application can use this pointer to access the structure containing application-specific information, such as a file handle or stream pointer. Note that the stubs do not modify the State pointer other than to pass it to the Alloc, Read, and Write functions. During encoding, Alloc is called to obtain a buffer into which the data is serialized. Then, Write is called to enable the application to control when and where the serialized data is stored. During decoding, Read is called to return the requested number of bytes of serialized data from where the application stored it.

An important feature of the incremental style is that the handle keeps the state pointer for you. This pointer maintains the state and is never touched by the RPC functions, except when passing the pointer to Alloc, Write, or Read function. The handle also maintains an internal state that makes it possible to encode and decode several type instances to the same buffer by adding padding as needed for alignment. The [**MesIncrementalHandleReset**](/windows/desktop/api/Midles/nf-midles-mesincrementalhandlereset) function resets a handle to its initial state to enable reading or writing from the beginning of the buffer.

The Alloc and Write functions, along with an application-defined pointer, are associated with an encoding-services handle by a call to the [**MesEncodeIncrementalHandleCreate**](/windows/desktop/api/Midles/nf-midles-mesencodeincrementalhandlecreate) function. **MesEncodeIncrementalHandleCreate** allocates the memory needed for the handle and then initializes it.

The application can call [**MesDecodeIncrementalHandleCreate**](/windows/desktop/api/Midles/nf-midles-mesdecodeincrementalhandlecreate) to create a decoding handle, [**MesIncrementalHandleReset**](/windows/desktop/api/Midles/nf-midles-mesincrementalhandlereset) to reinitialize the handle, or [**MesHandleFree**](/windows/desktop/api/Midles/nf-midles-meshandlefree) to free the handle's memory. The Read function, along with an application-defined parameter, is associated with a decoding handle by a call to the **MesDecodeIncrementalHandleCreate** routine. The function creates the handle and initializes it.

The UserState, Alloc, Write, and Read parameters of [**MesIncrementalHandleReset**](/windows/desktop/api/Midles/nf-midles-mesincrementalhandlereset) can be **NULL** to indicate no change.

 

 




