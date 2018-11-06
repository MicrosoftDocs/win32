---
title: Choosing When to Create Accessible Objects
description: Server developers can create all the accessible objects within a container when the container is created, or they can create the accessible objects dynamically.
ms.assetid: 26c8bb4b-19ec-4fd5-b758-30cb6a513818
ms.topic: article
ms.date: 05/31/2018
---

# Choosing When to Create Accessible Objects

Server developers can create all the accessible objects within a container when the container is created, or they can create the accessible objects dynamically.

For example, imagine a dialog box with several custom controls. A server creates accessible objects for all of the custom controls when the dialog box is displayed. However, if one of the controls is a custom combo box, the server waits until a user selects it to create accessible objects for the items that the combo box contains.

By having the parent create accessible objects dynamically, applications use less memory than if all the possible accessible objects were created ahead of time.

 

 




