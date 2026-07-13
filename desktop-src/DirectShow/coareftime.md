---
description: The COARefTime class converts reference times between seconds and 100-nanosecond units.
ms.assetid: 724420fc-9252-468f-9516-174be0a82999
title: COARefTime class (Ctlutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- COARefTime
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# COARefTime class

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

![coareftime class hierarchy](images/cutil05.png)

The `COARefTime` class converts reference times between seconds and 100-nanosecond units.

This class converts between reference times that are compatible with Automation and reference times that are compatible with C/C++. Automation-compatible interfaces use **double** values to represent time in seconds. Other interfaces use 64-bit **LONGLONG** values to represent time in 100-nanosecond units. The following types are defined for these values:

``` syntax
typedef LONGLONG  REFERENCE_TIME;
typedef double    REFTIME;
```

Filters can use the `COARefTime` class to convert between the two formats. This class is derived from the [**CRefTime**](creftime.md) class.



| Public Methods                                          | Description                                                           |
|---------------------------------------------------------|-----------------------------------------------------------------------|
| [**COARefTime**](coareftime-coareftime.md)             | Constructor method.                                                   |
| Operators                                               | Description                                                           |
| [**double**](coareftime-double.md)                     | Converts the reference time to a **double** value.                    |
| [**REFERENCE\_TIME**](coareftime-reference-time.md)    | Casts the object to a **REFERENCE\_TIME** value.                      |
| [**operator =**](coareftime-operator-assign.md)        | Assigns a new reference time.                                         |
| [**operator ==**](coareftime-operator-eq.md)           | Tests for equality between two reference times.                       |
| [**operator !=**](cmediatype-operator-neq.md)          | Tests for inequality between two reference times.                     |
| [**operator <**](coareftime-operator-lt.md)         | Tests if one reference time is less than another.                     |
| [**operator >**](coareftime-operator-gt.md)         | Tests if one reference time is greater than another.                  |
| [**operator <=**](coareftime-operator-lteq.md)      | Tests if one reference time is less than or equal to another.         |
| [**operator >=**](coareftime-operator-gteq.md)      | Tests if one reference time is greater than or equal to another.      |
| [**operator +**](coareftime-operator-plus.md)          | Adds two reference times.                                             |
| [**operator  **](coareftime-operator-minus.md)         | Subtracts one reference time from another.                            |
| [**operator +=**](coareftime-operator-plus-assign.md)  | Adds two reference times, and assigns the result to this object.      |
| [**operator  =**](coareftime-operator-minus-assign.md) | Subtracts two reference times, and assigns the result to this object. |
| [**operator \***](coareftime-operator-mult.md)         | Multiplies a reference time by a value.                               |
| [**operator /**](coareftime-operator-div.md)           | Divides a reference time by a value.                                  |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




