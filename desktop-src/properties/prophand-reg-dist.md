---
description: This topic explains how to create and register property handlers to work with the Windows property system.
ms.assetid: E6E81E04-9CC1-4df5-9A87-DE0CBD177356
title: Registering and Distributing Property Handlers
ms.topic: article
ms.date: 05/31/2018
---

# Registering and Distributing Property Handlers

This topic explains how to create and register property handlers to work with the Windows property system.

This topic is organized as follows:

-   [Registering and Distributing Property Handlers](#registering-and-distributing-property-handlers)
-   [Performance and Reliability Considerations for Property Handlers](#performance-and-reliability-considerations-for-property-handlers)
    -   [Guidelines for Performance and Reliability](#guidelines-for-performance-and-reliability)
-   [Related topics](#related-topics)

## Registering and Distributing Property Handlers

After the property handler is implemented, it must be registered and its file name extension must be associated with the handler. The following example using the .recipe extension illustrates the required registry entries to do so.

```
HKEY_CLASSES_ROOT
   CLSID
      {50d9450f-2a80-4f08-93b9-2eb526477d1a}
         (Default) = Recipe Property Handler
         ManualSafeSave [REG_DWORD] = 00000001
         InProcServer32
            (Default) = C:\\SDK\\PropertyHandlerSample\\bin\\RecipeHandlers.dll
            ThreadingModel = Apartment
HKEY_LOCAL_MACHINE
   SOFTWARE
      Microsoft
         Windows
            CurrentVersion
               PropertySystem
                  PropertyHandlers
                     .recipe
                        (Default) = {50d9450f-2a80-4f08-93b9-2eb526477d1a}
```

Property handlers for a particular file type are commonly distributed with the application(s) that create or manipulate files of that type. However, you should also consider making your property handlers available independently of these applications to support indexing of your file type in server scenarios where property handlers are used by the indexer, but their accompanying applications are not required. If you create a stand-alone installation package for your property handler, be sure that it includes the following:

-   The property handler registration details specified in the topic [Registering and Distributing Property Handlers]().
-   Registration for your file type and any schema files that must be installed, to enable clients to access all the features of your property handler.

## Performance and Reliability Considerations for Property Handlers

Property handlers are invoked for each file on a particular computer. They are usually called under the following circumstances:

-   During indexing of the file. This is done out-of-process, in an isolated process with restricted rights.
-   When files are accessed in Windows Explorer for the purpose of reading and writing property values. This is done in-process.

### Guidelines for Performance and Reliability

At any time, a user might have tens of thousands of files of any specific type (including yours) on his or her computers, and could access or modify any or all of these files at any time. Because property handlers are frequently invoked to support these access and modify operations, the performance and reliability characteristics of your property handler in busy, highly concurrent environments is of critical importance.

Keep in mind the following guidelines as you are developing and testing your property handler.

-   **Property enumeration**

    Property handlers should have a very fast response time in enumerating their properties. Memory-intensive calculations of property values, network lookups, or the search for resources other than the file itself should be avoided to ensure fast response times.

-   **In-place property writing**

    If possible, when dealing with medium-sized or large files (several hundred KB or larger), the file format should be arranged so that reading or writing property values does not require reading the whole file from disk. Even if the file needs to be sought, it should not be read into memory in its entirety because that bloats the working set of Windows Explorer or the Windows Search indexer as they try to access or index these files. For more information, see [Initializing Property Handlers](./building-property-handlers-property-handlers.md).

    One useful technique to accomplish this is to pad the header of the file with extra space so that the next time a property value needs to be written, the value can be written in place without needing to rewrite the entire file. This requires the ManualSafeSave functionality. This approach involves some extra risk that the file write operation might be interrupted while the write is in progress (due to a system crash or power loss), but because property sizes are generally small, the probability of such an interruption is similarly small, and the performance gains that can be realized through in-place property writing are considered significant enough to justify this additional risk. Even so, you should take care to test your implementation extensively to ensure that your files are not corrupted in the event that a failure does arise in the course of a write operation.

    Finally, when implementing in-place property writing with ManualSafeSave, sometimes the operation cannot be performed in-place, and the whole stream must be rewritten anyway. To facilitate the rewrite, the stream provided during handler initialization supports the [**IDestinationStreamFactory**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-idestinationstreamfactory) interface. The **IDestinationStreamFactory** interface enables handler implementations to obtain a temporary stream for writing; when all writes are completed and the [**IDestinationStreamFactory::GetDestinationStream**](/windows/win32/api/shobjidl_core/nf-shobjidl_core-idestinationstreamfactory-getdestinationstream) method is called, this stream is used to fully replace the original file stream. When the destination stream is used, the original file stream should be treated as read-only, because it will be replaced by the destination stream after the **IDestinationStreamFactory::GetDestinationStream** method has been called.

-   **Choosing your COM threading model**

    To maximize the efficiency of your property handler, you should specify that it uses the COM threading model `Both`. This enables direct access from STA apartments (Windows Explorer, for example) and message transfer agent (MTA) apartments (the SearchProtocolHost process in Windows Search, for example), avoiding the overhead of marshaling in those environments. To achieve the full benefit of the `Both` threading model, any services on which your handler depends should also be designated as `Both` to avoid any marshaling in calls to those components. Check the documentation of these particular services to verify whether they use this threading model.

-   **Property handler concurrency**

    Property handlers and the [**IPropertyStore**](/windows/win32/api/propsys/nn-propsys-ipropertystore) interface are designed for serial rather than concurrent access. Windows Explorer, the Windows Search indexer, and all other property handler invocations from the Windows codebase guarantee this usage. There should be no reason for third parties to use a property handler concurrently, but this behavior cannot be guaranteed. Also, even though the calling pattern is expected to be serial, the calls may come on different threads (for instance, when the object is being called remotely via COM RPC, as occurs in the indexer). Therefore, property handler implementations must support being called on different threads, and ideally should not suffer any ill effects when called concurrently. Because the intended calling pattern is serial, a trivial implementation using a critical section should be sufficient to meet these requirements in most cases. It is acceptable to avoid blocking on concurrent calls by using the [**TryEnterCriticalSection**](/windows/win32/api/synchapi/nf-synchapi-tryentercriticalsection) function to detect and fail concurrent calls.

-   **File concurrency**

    Property handlers are often used in scenarios where multiple applications access a file concurrently. Hence, the handler and the applications need to manage the concurrency by specifying appropriate sharing modes when opening the file. They also need to be aware of the access that the other applications specify and to manage cases where access is not allowed. It is best if all consumers specify liberal sharing modes to enable others to access the file concurrently, but when doing this, consistency issues need to be managed. Decisions on the most appropriate sharing modes to be used need to be made in the context of the community of applications that access the file.

    File systems enable applications to open files in a way that gives them control over whether and how other applications can open the file. Sharing modes enable read, write, and delete access. The property system supports a subset of these sharing modes, outlined in the following table.

    

    | Access mode                     | Sharing mode                             |
    |---------------------------------|------------------------------------------|
    | Write                           | Deny other readers and writers           |
    | Write (EnableShareDenyWrite)    | Enable other readers, deny other writers |
    | Read-only (default)             | Enable other readers, deny other writers |
    | Read-only (EnableShareDenyNone) | Enable other readers and writers         |

    

     

    Property handlers open for **write** (GPS\_READWRITE) will deny other readers and writers. Handlers can opt into behavior that enables readers by specifying the `EnableShareDenyWrite` flag (implying enable Read) in its registration.

    Property handlers open for **read** (GPS\_DEFAULT), by default enable other readers but deny other writers. Handlers can opt into enabling other writers by specifying the `EnableShareDenyNone` flag in its registration. This means that a handler can successfully handle a situation in which the content of a file changes while the handler is reading the file.

    For flag definitions, see [**GETPROPERTYSTOREFLAGS**](/windows/win32/api/propsys/ne-propsys-getpropertystoreflags).

## Related topics

<dl> <dt>

[Understanding Property Handlers](./building-property-handlers-properties.md)
</dt> <dt>

[Using Kind Names](./building-property-handlers-user-friendly-kind-names.md)
</dt> <dt>

[Using Property Lists](./building-property-handlers-property-lists.md)
</dt> <dt>

[Initializing Property Handlers](./building-property-handlers-property-handlers.md)
</dt> <dt>

[Property Handler Best Practices and FAQ](./prophand-bestprac-faq.md)
</dt> </dl>

 

 
