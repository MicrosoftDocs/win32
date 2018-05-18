---
Description: 'Note  This interface has been deprecated.'
ms.assetid: '6b0c5dfe-aa1b-4ad0-9272-f1351e494b11'
title: IDvdInfo interface
---

# IDvdInfo interface

> [!Note]  
> This interface has been deprecated. It will continue to be supported for backward compatibility with existing applications, but new applications should use [**IDvdInfo2**](idvdinfo2.md).

 

The **IDvdInfo** interface enables an application to query for attributes of available DVD titles and the DVD player status. It also allows for control of a DVD player beyond Annex J in the DVD specification. Use this interface to retrieve details about a DVD-Video or about the current state of the DVD player filter graph.

## Members

The **IDvdInfo** interface inherits from the [**IUnknown**](com.iunknown) interface. **IDvdInfo** also has these types of members:

-   [Methods](#methods)

### Methods

The **IDvdInfo** interface has these methods.



| Method                                                                            | Description                                                                                                                                                                       |
|:----------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetAllGPRMs**](idvdinfo-getallgprms.md)                                       | Retrieves the current contents of all general parameter registers (GPRMs).<br/>                                                                                             |
| [**GetAllSPRMs**](idvdinfo-getallsprms.md)                                       | Retrieves the current contents of all system parameter registers (SPRMs).<br/>                                                                                              |
| [**GetAudioLanguage**](idvdinfo-getaudiolanguage.md)                             | Retrieves the language of the specified audio stream within the current title.<br/>                                                                                         |
| [**GetCurrentAngle**](idvdinfo-getcurrentangle.md)                               | Retrieves the number of available angles and the currently selected angle number.<br/>                                                                                      |
| [**GetCurrentAudio**](idvdinfo-getcurrentaudio.md)                               | Retrieves the number of available audio streams and the number of the currently selected audio stream.<br/>                                                                 |
| [**GetCurrentAudioAttributes**](idvdinfo-getcurrentaudioattributes.md)           | Retrieves the attributes for the current audio stream in the current title or menu.<br/>                                                                                    |
| [**GetCurrentButton**](idvdinfo-getcurrentbutton.md)                             | Retrieves the number of available buttons and the currently selected button number.<br/>                                                                                    |
| [**GetCurrentDomain**](idvdinfo-getcurrentdomain.md)                             | Retrieves the current DVD domain of the DVD player.<br/>                                                                                                                    |
| [**GetCurrentLocation**](idvdinfo-getcurrentlocation.md)                         | Retrieves the current playback location.<br/>                                                                                                                               |
| [**GetCurrentSubpicture**](idvdinfo-getcurrentsubpicture.md)                     | Retrieves the number of available subpicture streams, the currently selected subpicture stream number, and whether the subpicture display is disabled.<br/>                 |
| [**GetCurrentSubpictureAttributes**](idvdinfo-getcurrentsubpictureattributes.md) | Retrieves the attributes for the current subpicture stream in the current title or menu.<br/>                                                                               |
| [**GetCurrentUOPS**](idvdinfo-getcurrentuops.md)                                 | Retrieves which [**IDvdControl**](idvdcontrol.md) methods are valid.<br/>                                                                                                  |
| [**GetCurrentVideoAttributes**](idvdinfo-getcurrentvideoattributes.md)           | Retrieves the current video attributes for the current title or menu.<br/>                                                                                                  |
| [**GetCurrentVolumeInfo**](idvdinfo-getcurrentvolumeinfo.md)                     | Retrieves the current DVD volume information.<br/>                                                                                                                          |
| [**GetDVDTextInfo**](idvdinfo-getdvdtextinfo.md)                                 | Retrieves the **TXTDT\_MG** structure, which can contain text descriptions for title name, volume name, producer name, vocalist name, and so on, in various languages.<br/> |
| [**GetNumberOfChapters**](idvdinfo-getnumberofchapters.md)                       | Retrieves the number of chapters that are defined for a given title.<br/>                                                                                                   |
| [**GetPlayerParentalLevel**](idvdinfo-getplayerparentallevel.md)                 | Retrieves the current parental level and country/region code settings for the DVD player.<br/>                                                                              |
| [**GetRoot**](idvdinfo-getroot.md)                                               | Retrieves the root directory that is set in the player.<br/>                                                                                                                |
| [**GetSubpictureLanguage**](idvdinfo-getsubpicturelanguage.md)                   | Retrieves the language of the specified subpicture stream within the current title.<br/>                                                                                    |
| [**GetTitleAttributes**](idvdinfo-gettitleattributes.md)                         | Retrieves attributes of all video, audio, and subpicture streams for the specified title, including menus.<br/>                                                             |
| [**GetTitleParentalLevels**](idvdinfo-gettitleparentallevels.md)                 | Retrieves the parental levels that are defined for a particular title.<br/>                                                                                                 |
| [**GetTotalTitleTime**](idvdinfo-gettotaltitletime.md)                           | Retrieves the total playback time for the current title.<br/>                                                                                                               |
| [**GetVMGAttributes**](idvdinfo-getvmgattributes.md)                             | Retrieves attributes of all video, audio, and subpicture streams for video manager (VMG) menus.<br/>                                                                        |



 

## See also

<dl> <dt>

[Deprecated Interfaces](deprecated-interfaces.md)
</dt> </dl>

 

 




