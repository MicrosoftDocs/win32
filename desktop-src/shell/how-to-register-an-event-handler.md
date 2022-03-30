---
description: A device can potentially generate many events, and each event has the option of being handled by one of a number of different handlers.
ms.assetid: C203B5AB-917C-4543-98D6-EDE02E0B5E49
title: How to Register an Event Handler
ms.topic: article
ms.date: 05/31/2018
---

# How to Register an Event Handler

A device can potentially generate many events, and each event has the option of being handled by one of a number of different handlers. In Windows XP, the following events are defined:

- DeviceArrival
- DeviceRemoval
- MediaArrival
- MediaRemoval

## Instructions


Event handlers are defined under the **EventHandlers** key. An event handler key's values are the names of each handler that the user must choose from when the event is detected. There is no data value associated with these entries. Following is an example definition for a custom event handler called **MyNewRemovalEventHandler**, which presents these handler possibilities to the user:

- A handler to use if the event is detected on a device made by the company named Contoso, Inc.
- A handler to use if the event is detected on a device made by the company named Fabrikam, Inc.
- A handler to use in all other cases.

```
HKEY_LOCAL_MACHINE
   SOFTWARE
      Microsoft
         Windows
            CurrentVersion
               Explorer
                  AutoplayHandlers
                     EventHandlers
                        MyNewRemovalEventHandler
                           CompanyContosoHandler [REG_SZ]
                           CompanyFabrikamHandler [REG_SZ]
                           MyRemovalHandler [REG_SZ]
```

After an event handler is defined, it must be registered with a device handler for one of the event possibilities: DeviceArrival, DeviceRemoval, MediaArrival, or MediaRemoval. MyNewRemovalEventHandler, defined earlier, is used for DeviceRemoval under a custom device handler named MyDeviceHandler and is defined for that purpose in the following example. Again, the registry value has no data component.

```
HKEY_LOCAL_MACHINE
   SOFTWARE
      Microsoft
         Windows
            CurrentVersion
               Explorer
                  AutoplayHandlers
                     DeviceHandlers
                        EventHandlers
                           DeviceRemoval
                              MyNewRemovalEventHandler
```

Windows XP predefines the following set of EventHandlers. 

| EventHandlers key        | Media or file type                             |
|--------------------------|------------------------------------------------|
| HandleCDBurningOnArrival | Blank CD-R/CD-RW                               |
| ShowPicturesOnArrival    | Picture files                                  |
| PlayMusicFilesOnArrival  | Music files                                    |
| PlayVideoFilesOnArrival  | Video files                                    |
| PlayCDAudioOnArrival     | Audio CD (REDBOOK format CD with Audio tracks) |
| PlayDVDMovieOnArrival    | DVD movies                                     |



 

Windows Vista predefines the following set of EventHandlers in addition to those above. 

| EventHandlers key              | Media or file type   |
|--------------------------------|----------------------|
| PlaySuperVideoCDMovieOnArrival | Super VideoCD movies |
| PlayVideoCDMovieOnArrival      | VideoCD movies       |



 

 

 



