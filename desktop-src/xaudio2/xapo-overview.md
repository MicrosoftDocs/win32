---
description: The XAPO API allows the creation of cross-platform audio processing objects (XAPO) for use in XAudio2 on both Windows and Xbox 360.
ms.assetid: 4fe88a0f-0234-462f-b575-e592f2c8401e
title: XAPO Overview
ms.topic: article
ms.date: 05/31/2018
---

# XAPO Overview

The XAPO API allows the creation of cross-platform audio processing objects (XAPO) for use in XAudio2 on both Windows and Xbox 360. An XAPO is an object that takes incoming audio data, and performs some operation on the data before passing it on. You can use an XAPO to perform a variety of tasks, including adding reverb to an audio stream and monitoring peak volume levels.

## Creating New XAPOs

The XAPO API provides the [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo) interface and the [**CXAPOBase**](/windows/desktop/api/XAPOBase/nl-xapobase-cxapobase) class for building new XAPO types. The **IXAPO** interface contains all of the methods that need to be implemented to create a new XAPO. The **CXAPOBase** class provides a basic implementation of the **IXAPO** interface. **CXAPOBase** implements all of the **IXAPO** interface methods except the [**IXAPO::Process**](/windows/win32/api/xapo/nf-xapo-ixapo-process) method, which is unique to each XAPO.

For an example of creating a new XAPO, see [How to: Create an XAPO](how-to--create-an-xapo.md).

For an example of creating a XAPO that accepts run-time parameters, see [How to: Add Run-time Parameter Support to an XAPO](how-to--add-run-time-parameter-support-to-an-xapo.md).

## XAPOs and COM

XAPOs implement the **IUnknown** interface. The [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo) and [**IXAPOParameters**](/windows/desktop/api/XAPO/nn-xapo-ixapoparameters) interfaces include the three **IUnknown** methods: **QueryInterface**, **AddRef**, and **Release**. [**CXAPOBase**](/windows/desktop/api/XAPOBase/nl-xapobase-cxapobase) provides implementations of all three of the IUnknown methods. A new instance of **CXAPOBase** will have a reference count of 1. It will be destroyed when its reference count becomes 0. Implementations of **IXAPO** and **IXAPOParameters** should follow the same pattern to allow for their proper management when used with XAudio2.

XAPO instances are passed to XAudio2 as **IUnknown** interfaces. XAudio2 uses **QueryInterface** to acquire an [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo) interface and to detect whether the XAPO implements the [**IXAPOParameters**](/windows/desktop/api/XAPO/nn-xapo-ixapoparameters) interface. Implementations of **IXAPO** must accept requests for **\_\_uuidof(IXAPO)**. If **IXAPOParameters** is implemented, it must also accept requests for **\_\_uuidof(IXAPOParameters)**.

## Using an XAPO in XAudio2

XAPOs are used in XAudio2 by attaching them to voices. Each XAudio2 voice has an effect chain containing zero or more audio effects. Audio data sent to a voice is passed through each effect in the chain before it is sent to the voice's output targets. Data is passed from the voice to each effect using the *pInputProcessParameters* parameter of the [**IXAPO::Process**](/windows/win32/api/xapo/nf-xapo-ixapo-process) method. Then it is returned to the voice using the *pOutputProcessParameters* parameter. The voice takes the output of each effect, and feeds it into the next effect in the chain until no effects are left in the chain.

For more information about XAudio2 effect chains, see [XAudio2 Audio Effects](xaudio2-audio-effects.md).

For an example of using an XAPO in XAudio2, see [How to: Use an XAPO in XAudio2](how-to--use-an-xapo-in-xaudio2.md).

## Effect Libraries

The XAPO effect library contains several XAPOs, and a common method of instantiating them. See [XAPOFX Overview](xapofx-overview.md) for information about XAPOFX. Also, XAudio2 has built-in reverb and volume meter effects. See [XAudio2 Audio Effects](xaudio2-audio-effects.md) for more information about the built-in XAudio2 effects.

## Related topics

<dl> <dt>

[Audio Effects](audio-effects.md)
</dt> <dt>

[XAudio2 Audio Effects](xaudio2-audio-effects.md)
</dt> </dl>

 

 
