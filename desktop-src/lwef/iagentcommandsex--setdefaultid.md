---
title: IAgentCommandsEx SetDefaultID
description: IAgentCommandsEx SetDefaultID
ms.assetid: 056ec518-bf0b-403f-adc6-9b53b0c044a7
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCommandsEx::SetDefaultID

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT SetDefaultID(
   long dwID,  // default command's ID
);
```

Sets the ID of the default command in a [**Commands**](https://msdn.microsoft.com/library/windows/desktop/ms695971) collection.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="dwID"></span><span id="dwid"></span><span id="DWID"></span>*dwID*
</dt> <dd>

The ID for the [**Command**](https://msdn.microsoft.com/library/windows/desktop/ms696441) to be set as the default.

</dd> </dl>

This property sets the default [**Command**](https://msdn.microsoft.com/library/windows/desktop/ms696441) object set in your [**Commands**](https://msdn.microsoft.com/library/windows/desktop/ms695971) collection. The default command is bold in the character's pop-up menu. However, setting the default command does not actually change command handling or double-click events.

This property applies only to your client application's use of the character; the setting does not affect other clients of the character or other characters of your client application.

## See Also

[**IAgentCommandsEx::GetDefaultID**](iagentcommandsex--getdefaultid.md)


 

 




