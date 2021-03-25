---
title: Network.bitRate
description: The bitRate property retrieves the current bit rate being received.
ms.assetid: e970a43a-1773-4dc0-ac2f-115f698bc1f4
keywords:
- Network.bitRate Windows Media Player
topic_type:
- apiref
api_name:
- Network.bitRate
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Network.bitRate

The **bitRate** property retrieves the current bit rate being received.

## Syntax

*player*.*network*.**bitRate**

## Possible Values

This property is a read-only **Number** (**long**).

## Remarks

This value is a combination of the bit rates of both the current video and audio streams.

## Examples

The following JScript example uses *Network*.**bitRate** to display the current media bit rate. The information is displayed in an HTML DIV created with ID = "BR". The **Player** object was created with ID = "Player".


```JScript
<!<entity type="mdash"/>-Create an event handler. -->
<SCRIPT FOR = Player EVENT = PlayStateChange()>
   switch (Player.playState){

      case 3:

         if (Player.network.bitRate){

            BR.innerHTML = "Current Bit Rate: " + Player.network.bitRate;
            BR.innerHTML += " K bits/second";
          }

         break;

      default:
   }
</SCRIPT>

```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Network Object**](network-object.md)
</dt> </dl>

 

 





