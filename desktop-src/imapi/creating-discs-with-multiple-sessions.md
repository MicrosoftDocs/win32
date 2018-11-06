---
title: Creating Discs with Multiple Sessions
description: IMAPI is capable of creating multi-session data discs. There are a few considerations to be aware of when creating a multi-session disc.
ms.assetid: 02405a32-53d5-4618-bfa0-c9a9f5e3c51b
ms.topic: article
ms.date: 05/31/2018
---

# Creating Discs with Multiple Sessions

IMAPI is capable of creating multi-session data discs. There are a few considerations to be aware of when creating a multi-session disc.

The [**IDiscMaster::SetActiveDiscRecorder**](/windows/desktop/api/Imapi/nf-imapi-idiscmaster-setactivediscrecorder) method determines whether there is an IMAPI multi-session disc in the active drive upon setting. If so, IMAPI goes into multi-session mode automatically. Using [**ClearFormatContent**](/windows/desktop/api/Imapi/nf-imapi-idiscmaster-clearformatcontent) after multi-session mode has been established causes IMAPI to return to single-session mode. This means that a blank disc is required for a [**RecordDisc**](/windows/desktop/api/Imapi/nf-imapi-idiscmaster-recorddisc) burn. If the disc is in multi-session mode, the same disc must be in the active recorder or an error code of IMAPI\_E\_WRONGDISC will be returned.

Selecting a recorder while in Joliet format causes IMAPI to read information from the currently installed disc. If the disc is a previous IMAPI Joliet disc that has space for another session, IMAPI automatically sets itself to multi-session mode. This disc must be present in the active recorder when calling [**RecordDisc**](/windows/desktop/api/Imapi/nf-imapi-idiscmaster-recorddisc).

Closing the first session on a disc requires 21 MB. Each additional session requires 11 MB to close.

 

 




