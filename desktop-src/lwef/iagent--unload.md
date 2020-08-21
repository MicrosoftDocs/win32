---
title: IAgent UnLoad
description: IAgent UnLoad
ms.assetid: 560301b3-c038-4c6e-b3f1-1203b618b67d
ms.topic: article
ms.date: 05/31/2018
---

# IAgent::UnLoad

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT UnLoad(
   long * dwCharID  //character ID
);
```

Unloads the character data for the specified character from the [**Characters**](/windows/desktop/lwef/the-characters-object) collection.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="dwCharID"></span><span id="dwcharid"></span><span id="DWCHARID"></span>*dwCharID*
</dt> <dd>

The character's ID.

</dd> </dl>

Use this method when you no longer need a character, to free up memory used to store information about the character. If you access the character again, use the [**Load**](load-method.md) method.

## See Also

[**IAgent::Load**](iagent--load.md)


 

 