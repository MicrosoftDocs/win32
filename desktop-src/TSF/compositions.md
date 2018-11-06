---
title: Compositions
description: A composition is a temporary input state that enables a text service to specify both to the application and the user that the input text is still in a state of change.
ms.assetid: 3d9da4f2-ceb9-4abc-8979-d3756d948a57
keywords:
- Text Services Framework (TSF),compositions
- TSF (Text Services Framework),compositions
- text services,compositions
- TSF-enabled applications,compositions
- compositions
ms.topic: article
ms.date: 05/31/2018
---

# Compositions

A composition is a temporary input state that enables a text service to specify both to the application and the user that the input text is still in a state of change. An application can and should obtain display attribute information about the composition and use this information to display the composition state to the user.

One example of the use of a composition is during speech input. While the user is speaking, the speech text service creates a composition. This composition will remain intact until the entire speech input is complete. When the session ends, the speech text service terminates the composition.

An application uses the presence and absence of a composition to determine how to display text and what, if any, processing should be performed on the text. For example, if the user is using the speech engine to input text, the application should not perform any spelling or grammar checking on any composition text. The text is considered incomplete until the composition is terminated.

## Text Services

A text service creates a composition by calling [ITfContextComposition::StartComposition](https://msdn.microsoft.com/library/windows/desktop/ms538713). The text service can optionally implement an [ITfCompositionSink](https://msdn.microsoft.com/library/windows/desktop/ms538654) object that receives composition event notifications. StartComposition returns an [ITfComposition](https://msdn.microsoft.com/library/windows/desktop/ms538653) object that the text service keeps a reference to and uses to modify and terminate the composition. The text service terminates the composition by calling [ITfComposition::EndComposition](https://msdn.microsoft.com/library/windows/desktop/ms538675).

If a text service is going to create compositions, it should also support display attributes to enable an application to display text that is part of a composition differently than standard text. For more information, see [Providing Display Attributes](providing-display-attributes.md).

## Applications

An application can monitor the creation, change and termination of compositions by installing an [ITfContextOwnerCompositionSink](https://msdn.microsoft.com/library/windows/desktop/ms538740) sink. When a composition is started, [ITfContextOwnerCompositionSink::OnStartComposition](https://msdn.microsoft.com/library/windows/desktop/ms538745) is called. Likewise, when a composition is changed or terminated, [ITfContextOwnerCompositionSink::OnUpdateComposition](https://msdn.microsoft.com/library/windows/desktop/ms538747) and [ITfContextOwnerCompositionSink::OnEndComposition](https://msdn.microsoft.com/library/windows/desktop/ms538743) will be called, respectively.

The following is a typical procedure to update a document using a composition.

1.  [ITextStoreACP::InsertTextAtSelection](/windows/desktop/api/Textstor/nf-textstor-itextstoreacp-inserttextatselection) or [ITextStoreAnchor::InsertTextAtSelection](/windows/desktop/api/Textstor/nf-textstor-itextstoreanchor-inserttextatselection) are typically used to insert the initial text into the composition.
2.  The composition is started with a call to [ITfContextComposition::StartComposition](/windows/desktop/api/Msctf/nf-msctf-itfcontextcomposition-startcomposition), using the range of text returned by **InsertTextAtSelection**.
3.  When it receives new input such as speech or keyboard entry, the application updates the composition with [ITextStoreACP::SetText](/windows/desktop/api/Textstor/nf-textstor-itextstoreacp-settext) or [ITextStoreAnchor::SetText](/windows/desktop/api/Textstor/nf-textstor-itextstoreanchor-settext).
4.  When the application determines that it is time to end the composition, it calls [ITfComposition::EndComposition](/windows/desktop/api/Msctf/nf-msctf-itfcomposition-endcomposition).

The application should use the display attributes provided by the text service to modify the display of text at all times and not just when a composition is active. For more information, see [Using Display Attributes](using-display-attributes.md).

If necessary, an application can terminate a composition by calling [ITfContextOwnerCompositionServices::TerminateComposition](https://msdn.microsoft.com/library/windows/desktop/ms538738).

 

 




