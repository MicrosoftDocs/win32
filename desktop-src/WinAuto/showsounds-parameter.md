---
title: ShowSounds Parameter and Audio Descriptions Flag
description: This topic includes information about a parameter that indicates whether an application should provide a visual alert or cue when it uses sound to convey important information.
ms.assetid: 7b316892-76ff-48b3-bf67-34dea2e63936
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ShowSounds Parameter and Audio Descriptions Flag

This topic includes information about a parameter that indicates whether an application should provide a visual alert or cue when it uses sound to convey important information. It also provides information about a flag that indicates whether an application should provide an audio description for visual elements.

## ShowSounds Parameter

The ShowSounds parameter indicates whether the user wants applications to present all important information in visual form.

The user controls the setting of the ShowSounds parameter by using the Ease of Access Center in Control Panel, or another application for customizing the environment. Applications use the **SPI\_GETSHOWSOUNDS** and **SPI\_SETSHOWSOUNDS** flags with the [**SystemParametersInfo**](https://msdn.microsoft.com/library/windows/desktop/ms724947) function to get and set the ShowSounds parameter. Alternatively, applications can use the **SM\_SHOWSOUNDS** flag with the [**GetSystemMetrics**](https://msdn.microsoft.com/library/windows/desktop/ms724385) function to determine the state of the ShowSounds parameter.

Determining the state of the ShowSounds parameter is necessary only for applications that would typically present important information by sound alone. Applications should provide ShowSounds support if they use sounds in either of the following ways:

-   To convey information that is important to the operation of the application.
-   To alert the user that important information is being presented visually. If this is the case, even though the information is presented visually, the sound has the additional function of attracting the attention of the user.

Appropriate visual feedback forms can make the software much more functional for users who cannot rely on sound alone. The design of the visual feedback is application specific and depends on the information that will be presented to the user. For example, to attract the user's attention when new electronic mail arrives, the application might flash its window or even flash the entire screen. If the application typically makes sound to indicate that the user is trying to perform an illegal operation, it could also display an appropriate message on its status line or use the [**MessageBox**](https://msdn.microsoft.com/library/windows/desktop/ms645505) function to display a specific error message. If the application is typically designed to play sound bites that carry meaning, such as digitized speech, it could also display a caption window with the same text.

Redundant use of audible and visual alerts has been shown to increase the usability of software applications. The ShowSounds parameter is a request for visual feedback, but its use does not restrict an application to presenting information visually. Users should be able to request visual feedback regardless of whether they also want audible feedback.

## Audio Description Flag

Applications use the **SPI\_GETAUDIODESCRIPTION** and **SPI\_SETAUDIODESCRIPTION** flags with the [**SystemParametersInfo**](https://msdn.microsoft.com/library/windows/desktop/ms724947) function to enable or disable audio descriptions. While it is possible for users who are visually impaired to hear the audio in video content, there is a lot of action in video that does not have corresponding audio. Specific audio description of what is happening in a video helps these users understand the content better. This flag enables you to enable or disable audio descriptions in the languages they are provided in.

 

 




