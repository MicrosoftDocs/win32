---
description: Activation Objects
ms.assetid: 767d5f1c-2b8d-43b6-916b-035129e93204
title: Activation Objects
ms.topic: article
ms.date: 05/31/2018
---

# Activation Objects

An *activation object* is a helper object that is used to create another object, somewhat similar to a class factory. Activation objects expose the [**IMFActivate**](/windows/desktop/api/mfobjects/nn-mfobjects-imfactivate) interface.

An activation object lets you defer the creation of the target object, because you can hold onto an [**IMFActivate**](/windows/desktop/api/mfobjects/nn-mfobjects-imfactivate) pointer without creating the target object. Activation objects can also be serialized, and thus used to create the target object in another process. For example, activation objects are used to marshal pipeline components from the application process to the protected media path (PMP) process. Activation objects are also used by certain enumeration functions that return a list of **IMFActivate** pointers. Before the application creates the target object, it can get information about the object by examining attributes on the activation object.

To create the target object from an activation object, call the [**IMFActivate::ActivateObject**](/windows/desktop/api/mfobjects/nf-mfobjects-imfactivate-activateobject) method. The caller must call [**IMFActivate::ShutdownObject**](/windows/desktop/api/mfobjects/nf-mfobjects-imfactivate-shutdownobject) when it is done using the created object. Often the application creates the activation object, and the Media Session calls **ActivateObject**. In that case, the Media Session, not the application, must call **ShutdownObject**. In other situations, the application receives an [**IMFActivate**](/windows/desktop/api/mfobjects/nn-mfobjects-imfactivate) pointer from the Media Session, and the application calls **ActivateObject** and **ShutdownObject**. (For example, see [How to Play Protected Media Files](how-to-play-protected-media-files.md).)

Activation objects can have attributes, and the [**IMFActivate**](/windows/desktop/api/mfobjects/nn-mfobjects-imfactivate) interface inherits the [**IMFAttributes**](/windows/desktop/api/mfobjects/nn-mfobjects-imfattributes) interface. Some activation objects use attributes to configure the created object. The specific attributes supported by each object are documented in the reference for that activation object's creation function. Set the attributes using the **IMFActivate** pointer that you receive from the function.

For protected playback, activation objects are marshaled to the PMP process. To support marshaling, an activation object must expose the **IPersistStream** interface. In addition, both the activation object and the created object must be trusted components if the PMP is running in a protected process. This is not a requirement when the PMP is loaded in an unprotected process.

To use a custom pipeline object (such as a media sink) inside the PMP process, you must implement an activation object for your pipeline object:

-   The activation object must expose [**IMFActivate**](/windows/desktop/api/mfobjects/nn-mfobjects-imfactivate) and **IPersistStream**.
-   The activation object's **IPersist::GetClassID** method must return the activation object's CLSID.
-   Optionally, you can implement the **IPersistStream::Save** and **IPersistStream::Load** methods to marshal any data that you need to configure your activation object.

When the Media Session loads the topology inside the PMP process, it calls **CoCreateInstance** to create a new instance of your activation object. Then it calls [**IMFActivate::ActivateObject**](/windows/desktop/api/mfobjects/nf-mfobjects-imfactivate-activateobject) to create the pipeline object.

## Related topics

<dl> <dt>

[Media Foundation Platform APIs](media-foundation-platform-apis.md)
</dt> <dt>

[**IMFActivate**](/windows/desktop/api/mfobjects/nn-mfobjects-imfactivate)
</dt> </dl>

 

 



