---
Description: You can notify the XAudio2 client code of engine events by registering an instance of a class implementing the IXAudio2EngineCallback interface with the XAudio2 engine.
ms.assetid: 006a8cb6-c24c-f7d1-9e8b-9cb2baa046c0
title: How to Use Engine Callbacks
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# How to: Use Engine Callbacks

You can notify the XAudio2 client code of engine events by registering an instance of a class implementing the [**IXAudio2EngineCallback**](/windows/win32/xaudio2/nn-xaudio2-ixaudio2enginecallback?branch=master) interface with the XAudio2 engine. This allows the XAudio2 client code to keep track of when audio processing is occurring, and when to restart the engine in the event of a critical error.

## To use an engine callback

The following steps register an object to handle engine events.

1.  Create a class that inherits from the [**IXAudio2EngineCallback**](/windows/win32/xaudio2/nn-xaudio2-ixaudio2enginecallback?branch=master) interface.

    All methods of [**IXAudio2EngineCallback**](/windows/win32/xaudio2/nn-xaudio2-ixaudio2enginecallback?branch=master) are purely virtual and must be defined. The method of interest in this example is [**IXAudio2EngineCallback::OnCriticalError**](ixaudio2enginecallback-oncriticalerror.md), which sets a flag to signal the main game loop that a critical error has occurred. The remaining methods, [**IXAudio2EngineCallback::OnProcessingPassStart**](ixaudio2enginecallback-onprocessingpassstart.md) and [**IXAudio2EngineCallback::OnProcessingPassEnd**](ixaudio2enginecallback-onprocessingpassend.md), are stubs in this example.

    ```
    class EngineCallback : public IXAudio2EngineCallback
    {
        void OnProcessingPassEnd () {}
        void OnProcessingPassStart() {}
        void OnCriticalError (HRESULT Error) {}
    };
    ```

    

2.  Use [**XAudio2Create**](/windows/win32/xaudio2/nf-xaudio2-xaudio2create?branch=master) to create an instance of the XAudio2 engine.

    ```
    if ( FAILED(hr = XAudio2Create( &amp;pXAudio2, 0, XAUDIO2_DEFAULT_PROCESSOR ) ) )
        return hr;
    ```

    

3.  Use [**IXAudio2::RegisterForCallbacks**](ixaudio2-interface-registerforcallbacks.md) to register the engine callback.

    ```
    pXAudio2->RegisterForCallbacks( &amp;engineCallback );
    ```

    

4.  If you don't need the engine callback any more, call [**IXAudio2::UnregisterForCallbacks**](ixaudio2-interface-unregisterforcallbacks.md).

    ```
    pXAudio2->UnregisterForCallbacks( &amp;engineCallback );
    ```

    

## Related topics

<dl> <dt>

[Callbacks](callbacks.md)
</dt> <dt>

[XAudio2 Callbacks](xaudio2-callbacks.md)
</dt> <dt>

[XAudio2 Programming Guide](programming-guide.md)
</dt> <dt>

[How to: Build a Basic Audio Processing Graph](how-to--build-a-basic-audio-processing-graph.md)
</dt> <dt>

[How to: Stream a Sound from Disk](how-to--stream-a-sound-from-disk.md)
</dt> </dl>

 

 



