---
description: Windows Peer Components for People Near Me
ms.assetid: aa9e7d4d-4131-4578-8bd1-298f04b826f9
title: Windows Peer Components for People Near Me
ms.topic: article
ms.date: 05/31/2018
---

# Windows Peer Components for People Near Me

Within the main Windows Peer Networking executable (P2phost.exe), the [People Near Me Architecture](people-near-me-architecture.md) uses the following components:

### People Near Me

The People Near Me (PNM) component initiates discovery using Web Services Discovery on the local subnet for the user names of PNM-capable computers.

### People Near Me Publisher

The People Near Me Publisher component publishes the nicknames of logged-on users to indicate availability to other computers using PNM on the local subnet. The logged-on user must elect to publish their nickname before it is advertised. The nickname is published on the subnet using Web Services Discovery. Additionally, objects and applications can also be published. However, the user must specify object and application publication for the '**People Near Me**' or '**All**' scopes.

### People Near Me Enumerator

The People Near Me Enumerator component enumerates the list of users on the local subnet. Using this list, Web Services Discovery sends a multicast query and receives the responses. After the list of nicknames are obtained, an application can use the API to retrieve more data being published by the user (which is encrypted using [SChannel](windows-vista-components-for-people-near-me.md)), such as the list of applications registered and any objects being published.

The search and enumeration process does not happen automatically, but must be explicitly initiated by a user or an application by signing-in to PNM. The search results are the list of nicknames of other users on the same subnet that are advertising their nicknames using the PNM API.

### Publication Manager

The Publication Manager component is responsible for publishing presence, application, or object updates to contacts or people near me that are subscribed or poll for data.

### Peer Signaling

The Peer Signaling component handles the creation of connections between peers to exchange data. For People Near Me, Peer Signaling is used when a user or application sends the unicast query to a specific computer for its public key, applications, and objects.

### Receive Invitation Handler/UX

The Receive Invitation Handler/UX component receives an incoming invitation from another person, prompts the user to determine whether they want to launch the application associated with the invitation, and then launches the application based on the user accepting the invitation. An invitation is a message from another person to initiate collaboration activity using a specific application that is installed on both user's computers and is advertised by the user being invited.

### Peer Security

When presence, application, and object are sent, the information is encrypted using an SSL channel ([Schannel](windows-vista-components-for-people-near-me.md)). The initiating computer uses the public key of the invited computer to negotiate a secret key that is used for encrypting the subsequent data sent between the two peers.

 

 



