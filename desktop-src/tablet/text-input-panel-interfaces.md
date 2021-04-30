---
description: This section contains information about the interfaces used to control the appearance and behavior of the Tablet PC Input Panel.
ms.assetid: 58f49d5b-8b38-45e7-94e1-8a4434d6e13b
title: Text Input Panel Interfaces
ms.topic: article
ms.date: 05/31/2018
---

# Text Input Panel Interfaces

This section contains information about the interfaces used to control the appearance and behavior of the Tablet PC Input Panel.

> [!Note]  
> The Text Input Panel interfaces are not Automation compliant.

 

## In This Section



| Interface                                                                | Description                                                                                                                                  |
|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| [**IHandWrittenTextInsertion Interface**](/windows/desktop/api/peninputpanel/nn-peninputpanel-ihandwrittentextinsertion) | Used by the application's custom text entry code to insert the text into both the text field and the Text Services backing-store.<br/> |
| [**ITextInputPanel Interface**](/windows/desktop/api/peninputpanel/nn-peninputpanel-itextinputpanel)                     | Provides control over the Tablet PC Input Panel.<br/>                                                                                  |
| [**ITextInputPanelEventSink Interface**](/windows/desktop/api/peninputpanel/nn-peninputpanel-itextinputpaneleventsink)   | Defines methods that handle the [**ITextInputPanel Interface**](/windows/desktop/api/peninputpanel/nn-peninputpanel-itextinputpanel) events.<br/>                                      |
| [**ITextInputPanelRunInfo Interface**](/windows/desktop/api/peninputpanel/nn-peninputpanel-itextinputpanelruninfo)       | Provides a method to determine if the Text Input Panel is currently running.<br/>                                                      |
| [**ITipAutocompleteClient Interface**](itipautocompleteclient.md)       | Enables the client to call the application's Text Input Panel auto complete provider object.<br/>                                      |
| [**ITipAutocompleteProvider Interface**](itipautocompleteprovider.md)   | Manages the application's side of the Text Input Panel auto complete integration.<br/>                                                 |



 

## Related topics

<dl> <dt>

[Text Input Panel Reference](text-input-panel-reference.md)
</dt> </dl>

 

 




