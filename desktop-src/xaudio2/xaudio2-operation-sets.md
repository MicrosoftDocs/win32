---
description: This overview introduces several XAudio2 methods that you can call as part of an operation set.
ms.assetid: 5bfd747d-af65-f619-e549-be8130748261
title: XAudio2 Operation Sets
ms.topic: article
ms.date: 05/31/2018
---

# XAudio2 Operation Sets

This overview introduces several XAudio2 methods that you can call as part of an operation set.

Several XAudio2 methods take the *OperationSet* argument, which allows them to be called as part of a deferred group. At a specific time, you can apply an entire set of changes simultaneously by calling the function [**IXAudio2::CommitChanges**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2-commitchanges) with the *OperationSet* identifier for that group. The identifier is an arbitrary number. Thus, it allows separate parts of the client code to apply separate atomic changes to the graph without any conflict. The recommended practice is for the client to increment a global counter whenever it needs to generate a unique, new *OperationSet* identifier. A set of changes to the graph, applied atomically, is guaranteed to be sample-accurate. For example, voices will start in sync.

If you set *OperationSet* to XAUDIO2\_COMMIT\_NOW, the change applies immediately. It takes effect in the first audio processing pass after the method call. If you call [**CommitChanges**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2-commitchanges) with XAUDIO2\_COMMIT\_ALL, changes to all pending operations sets are performed, regardless of their *OperationSet* identifier.

Certain methods take effect immediately when they are called from an XAudio2 callback with an *OperationSet* of XAUDIO2\_COMMIT\_NOW. All other methods that take an *OperationSet* argument only take effect on the next processing pass after the method is called (if called with XAUDIO2\_COMMIT\_NOW), or after [**CommitChanges**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2-commitchanges) is called with the same *OperationSet*. Because of this, certain method calls may not always happen in the same order in which they were called.

All pending operations are committed atomically when [**IXAudio2::StopEngine**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2-stopengine) is called. Any methods that are called while the engine is stopped take effect immediately, regardless of the *OperationSet* value provided. When you restart the engine, XAudio2 returns to asynchronous mode.

Simple scenarios in which operation sets are useful include the following examples.

-   Starting multiple voices simultaneously.
-   Simultaneously submitting a buffer to a voice, setting the voice parameters, and starting the voice.
-   Making a large-scale change to the graph, such as connecting all source voices to a new submix voice.

See [How to: Group Audio Methods as an Operation Set](how-to--group-audio-methods-as-an-operation-set.md) for an example of using an operation set.

## Operation Set Methods

You can call the following methods as part of an operation set.

-   [**IXAudio2SourceVoice::ExitLoop**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2sourcevoice-exitloop)
-   [**IXAudio2Voice::SetFilterParameters**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2voice-setfilterparameters)
-   [**IXAudio2SourceVoice::SetFrequencyRatio**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2sourcevoice-setfrequencyratio)
-   [**IXAudio2Voice::DisableEffect**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2voice-disableeffect)
-   [**IXAudio2Voice::EnableEffect**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2voice-enableeffect)
-   [**IXAudio2Voice::SetChannelVolumes**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2voice-setchannelvolumes)
-   [**IXAudio2Voice::SetEffectParameters**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2voice-seteffectparameters)
-   [**IXAudio2Voice::SetOutputMatrix**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2voice-setoutputmatrix)
-   [**IXAudio2Voice::SetVolume**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2voice-setvolume)
-   [**IXAudio2SourceVoice::Start**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2sourcevoice-start)
-   [**IXAudio2SourceVoice::Stop**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2sourcevoice-stop)

As described previously, client code must ultimately call the function [**IXAudio2::CommitChanges**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2-commitchanges) to execute the deferred changes.

## Related topics

<dl> <dt>

[Operation Sets](operation-sets.md)
</dt> <dt>

[XAudio2 Programming Guide](programming-guide.md)
</dt> <dt>

[How to: Group Audio Methods as an Operation Set](how-to--group-audio-methods-as-an-operation-set.md)
</dt> </dl>

 

 
