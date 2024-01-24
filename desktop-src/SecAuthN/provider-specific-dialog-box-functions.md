---
description: Provider-specific dialog box functions enable a provider to display and handle network-specific information by altering system dialog boxes or displaying custom dialog boxes.
ms.assetid: c9a52867-0a0b-40d8-a09d-2b7bed517e13
title: Provider-Specific Dialog Box Functions
ms.topic: article
ms.date: 05/31/2018
---

# Provider-Specific Dialog Box Functions

Provider-specific dialog box functions enable a provider to display and handle network-specific information by altering system dialog boxes or displaying custom dialog boxes.

The following dialog box functions add buttons to the File Manager **Properties** dialog box. The provider can then handle the events of those buttons to perform network-specific tasks. Note that there is a limit to the number of buttons that can be added. Because of this, providers should use this capability sparingly. Also, a provider may find itself unable to add a button because the available space has been used already by other providers. A network provider should handle this situation.



| Function                                           | Description                                                                                                                             |
|----------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| [**NPGetPropertyText**](/windows/desktop/api/Npapi/nf-npapi-npgetpropertytext)     | Determines the names of buttons added to a property dialog box for a specific resource.<br/>                                      |
| [**NPPropertyDialog**](/windows/desktop/api/Npapi/nf-npapi-nppropertydialog)       | Called when a user clicks a button added by using the [**NPGetPropertyText**](/windows/desktop/api/Npapi/nf-npapi-npgetpropertytext) function.<br/>               |
| [**NPSearchDialog**](/windows/desktop/api/Npapi/nf-npapi-npsearchdialog)           | Enables network providers to implement their own search functionality beyond that provided in the **Connection** dialog box.<br/> |
| [**NPFormatNetworkName**](/windows/desktop/api/Npapi/nf-npapi-npformatnetworkname) | Enables network providers to format or otherwise modify network names before they are presented to the user.<br/>                 |



 

 

 




