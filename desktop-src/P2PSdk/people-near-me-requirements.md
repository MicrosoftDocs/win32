---
description: People Near Me Requirements
ms.assetid: c7ab73fc-56a6-4b6c-820a-3f8e4a97cfaf
title: People Near Me Requirements
ms.topic: article
ms.date: 05/31/2018
---

# People Near Me Requirements

In order for [People Near Me](about-people-near-me.md) to provide seamless connectivity and easy collaboration to users for Windows Peer Networking applications, the following is accomplished:

### People Discovery

People Discovery allows a user to discover and display the set of peers that are located on the local subnet. Any computers on the local subnet must advertise the names of logged-on peers. The peers listed after a discovery query are the set of users running Windows Vista that are configured to advertise a nickname to other users using [People Near Me](about-people-near-me.md). This capability is disabled by default and must be enabled by the logged-in user.

> [!Note]  
> Remote peers discovered during the 'People Near Me' discovery process are not necessarily the anticipated users associated with the discovered peers.

 

### Extended Data Discovery

Extended Data Discovery allows searches for users that have specific interests. It is also possible for users to specify that they want to advertise additional data about themselves. For example the data could outline specific professional interests at an industry conference, in addition to the nickname of the logged in user.

### Application Discovery

The exact nature of the ad hoc collaboration enabled by People Near Me is specific to applications. For example, the collaboration might be chatting or sharing photos, both requiring specific applications. In order for People Near Me to enable collaboration activities, the set of applications that are available for People Near Me scenarios must also be advertised and discoverable.

### Subscription

Using a subscription, applications can subscribe to track a person's presence, applications, and object changes.

### Invitation

After the people, interests, and applications have been discovered, peer collaboration, using a People Near Me application, can begin an invitation and acceptance exchange. The initiating peer sends an invitation message to another peer or peers. The users receiving the invitation can accept or decline the invitation. When the invitation is accepted the appropriate peer application for the requested activity is launched.

### Add As A Contact

If users establish a collaboration activity through People Near Me and want to maintain contact over time, they can add each other as a contact. Once this is accomplished they can observe the presence status of a user (such as online, offline, or away) and invite them to a collaboration activity at any time across the Internet. Any activity that was possible with the person when they were located nearby is also possible with a contact over the Internet.

### Security

To protect the users and the data being exchanged in a peer collaboration activity, users have configuration control over what is being advertised. Users must also accept an invitation before peer collaboration can begin. The collaboration activity is encrypted with a Secure Sockets Layer (SSL)-encrypted channel (also known as Schannel). SSL is a cryptographic protocol to protect TCP-based communications. For more information, see [SChannel](windows-vista-components-for-people-near-me.md). These requirements are supported by a new set of components in the [Windows Peer Networking](what-is-peer-networking-.md)architecture in Windows Vista.

 

 



