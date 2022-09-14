---
title: Standard DISPIDS
description: A number of standard dispids have been defined for the controls specification.
ms.assetid: f938b64f-5d45-40e7-ad02-665ce9c86a70
ms.topic: article
ms.date: 05/31/2018
---

# Standard DISPIDS

A number of standard dispids have been defined for the controls specification.

## DISPID\_MOUSEPOINTER

Property of type integer.

``` syntax
#define DISPID_MOUSEPOINTER            -521
```

The Mousepointer property identifies standard mouse icons.



| Value         | Description                                                                |
|---------------|----------------------------------------------------------------------------|
| 0<br/>  | (Default) Shape determined by the object.<br/>                       |
| 1<br/>  | Arrow<br/>                                                           |
| 2<br/>  | Cross (cross-hair pointer)<br/>                                      |
| 3<br/>  | I Beam<br/>                                                          |
| 4<br/>  | Icon (small square within a square)<br/>                             |
| 5<br/>  | Size (four-pointed arrow pointing north, south, east, and west)<br/> |
| 6<br/>  | Size NE SW (double arrow pointing northeast and southwest)<br/>      |
| 7<br/>  | Size N S (double arrow pointing north and south)<br/>                |
| 8<br/>  | Size NW, SE<br/>                                                     |
| 9<br/>  | Size E W (double arrow pointing east and west)<br/>                  |
| 10<br/> | Up Arrow<br/>                                                        |
| 11<br/> | Hourglass (wait)<br/>                                                |
| 12<br/> | No Drop<br/>                                                         |
| 13<br/> | Arrow and hourglass<br/>                                             |
| 14<br/> | Arrow and question mark<br/>                                         |
| 15<br/> | Size all<br/>                                                        |
| 99<br/> | Custom icon specified by the MouseIcon property<br/>                 |



 

## DISPID\_MOUSEICON

Property of type picture.

``` syntax
#define DISPID_MOUSEICON               -522
```

## DISPID\_PICTURE

Property of type picture.

``` syntax
#define DISPID_PICTURE                 -523
```

## DISPID\_VALID

Used to determine if the control has valid data or not.

Property of type BOOL.

``` syntax
#define DISPID_VALID                   -524
```

## DISPID\_ AMBIENT\_PALETTE

Used to allow the control to get the container's HPAL. If the container supplies an ambient palette then that is the only palette that may be realized into the foreground. Controls that want to realize their own palettes must do so in the background. If there is no ambient palette provided by the container, then the active control can realize its palette in the foreground. Palette handling is further discussed in Palette Behavior for OLE Controls which is in the ActiveX SDK.

``` syntax
#define DISPID_AMBIENT_PALETTE         -726
```

 

 





