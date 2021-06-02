---
description: XAudio2 can call functions provided by the client to notify it asynchronously of certain events taking place in the audio processing thread.
ms.assetid: 4fbd4229-f7ac-33b3-b4b7-f09150a60598
title: XAudio2 Callbacks
ms.topic: article
ms.date: 05/31/2018
---

# XAudio2 Callbacks

XAudio2 can call functions provided by the client to notify it asynchronously of certain events taking place in the audio processing thread. These callbacks can be global or specific to a given source voice. To receive global engine callbacks, the client must provide an instance of a class implementing the [**IXAudio2EngineCallback**](/windows/desktop/api/xaudio2/nn-xaudio2-ixaudio2enginecallback) interface when initializing XAudio2. To receive source voice callbacks, the client must provide an instance of a class implementing the [**IXAudio2VoiceCallback**](/windows/desktop/api/xaudio2/nn-xaudio2-ixaudio2voicecallback) interface when creating source voices. For more details, see **IXAudio2EngineCallback** and **IXAudio2VoiceCallback**.

You must implement callbacks carefully to avoid causing breaks in the audio. Whenever a callback is running, XAudio2 cannot generate any audio. Delays of more than a few milliseconds can cause an audio problem. Delays of this nature also generate debugger output. This indicates potential performance issues. At a minimum, callback functions must not do the following:

-   Access the hard disk or other permanent storage
-   Make expensive or blocking API calls
-   Synchronize with other parts of client code
-   Require significant CPU usage

If the client design requires a callback to trigger actions such as those listed previously, the callback should signal a different client thread to do the work. You can do this with a simple **SetEvent** mechanism or more sophisticated mechanisms like a nonblocking command queue that is consumed by another thread.

## IXAudio2EngineCallback

The [**IXAudio2EngineCallback**](/windows/desktop/api/xaudio2/nn-xaudio2-ixaudio2enginecallback) class contains methods that notify the client when certain events happen in the XAudio2 engine. These methods should be implemented by the XAudio2 client. XAudio2 calls these methods by means of an interface pointer provided by the client using the [**IXAudio2::RegisterForCallbacks**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2-registerforcallbacks) method. All these methods return **void**, rather than an **HRESULT**.

## IXAudio2VoiceCallback

The [**IXAudio2VoiceCallback**](/windows/desktop/api/xaudio2/nn-xaudio2-ixaudio2voicecallback) class contains methods that notify the client when certain events happen in a specific XAudio2 source voice. XAudio2 calls these methods by means of an interface pointer provided by the client in [**IXAudio2::CreateSourceVoice**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2-createsourcevoice). As with [**IXAudio2EngineCallback**](/windows/desktop/api/xaudio2/nn-xaudio2-ixaudio2enginecallback), these methods should be implemented by the XAudio2 client, and return **void** rather than an **HRESULT**.

As mentioned previously, it is crucial that the client-provided implementations of these callbacks return as quickly as possible, preferably within a millisecond. The callbacks are executed in the audio processing thread, and all processing is interrupted until the callback returns. A delay in a callback can easily cause an audio problem.

## Related topics

<dl> <dt>

[Callbacks](callbacks.md)
</dt> <dt>

[XAudio2 Programming Guide](programming-guide.md)
</dt> <dt>

[How to: Use Source Voice Callbacks](how-to--use-source-voice-callbacks.md)
</dt> <dt>

[How to: Use Engine Callbacks](how-to--use-engine-callbacks.md)
</dt> <dt>

[How to: Stream a Sound from Disk](how-to--stream-a-sound-from-disk.md)
</dt> </dl>

 

 
