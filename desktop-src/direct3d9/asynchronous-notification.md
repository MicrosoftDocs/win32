---
description: There are number of interesting queries on a driver that an application can make if there is no performance cost.
ms.assetid: 81e1c5c5-03bc-4598-814e-14e56513e221
title: Asynchronous Notification (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Asynchronous Notification (Direct3D 9)

There are number of interesting queries on a driver that an application can make if there is no performance cost. In Direct3D 7 and Direct3D 8, a synchronous query mechanism, GetInfo, worked well for things like statistics, but no performance-critical queries were added. There are other things (like fences) that are inherently asynchronous. This is a simple API to make both synchronous and asynchronous queries. GetInfo will be retired in Direct3D 9.

Create a query using [**IDirect3DDevice9::CreateQuery**](/windows/desktop/api). This method takes a D3DQUERYTYPE, which defines what kind of query to make and returns a pointer to an [**IDirect3DQuery9**](/windows/desktop/api) object. If the query type is not supported, the call returns an error D3DERR\_NOTAVAILABLE. Using the query object, the application submits the query to the runtime using [**IDirect3DQuery9::Issue**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3dquery9-issue), and polls the query status using [**IDirect3DQuery9::GetData**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3dquery9-getdata). If the query result is available, S\_OK is returned; otherwise, S\_FALSE is returned. The application is expected to pass an appropriately sized buffer for the query results.

The application has an option to force the runtime to flush the query down to the driver by using D3DGETDATA\_FLUSH with [**IDirect3DQuery9::GetData**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3dquery9-getdata). It causes a flush, forcing the driver to see the query. In this case, D3DERR\_DEVICELOST is returned if the device becomes lost.

All queries are lost when the device is lost, the application has to re-create them. If the device does not support the query and the pQueryID is **NULL**, the query creation will fail with D3DERR\_INVALIDCALL.

The following table summaries important information about each query type.



| QuertyType                    | Valid issue flag              | GetData buffer              | Runtime      | Implicit beginning of query |
|-------------------------------|-------------------------------|-----------------------------|--------------|-----------------------------|
| D3DQUERYTYPE\_VCACHE          | D3DISSUE\_END                 | D3DDEVINFO\_VCACHE          | Retail/Debug | CreateDevice                |
| D3DQUERYTYPE\_ResourceManager | D3DISSUE\_END                 | D3DDEVINFO\_ResourceManager | Debug only   | Present                     |
| D3DQUERYTYPE\_VERTEXSTATS     | D3DISSUE\_END                 | D3DDEVINFO\_D3DVERTEXSTATS  | Debug only   | Present                     |
| D3DQUERYTYPE\_EVENT           | D3DISSUE\_END                 | BOOL                        | Retail/Debug | CreateDevice                |
| D3DQUERYTYPE\_OCCLUSION       | D3DISSUE\_BEGIN,D3DISSUE\_END | DWORD                       | Retail/Debug | N/A                         |



 

Flags field for [**IDirect3DQuery9::Issue**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3dquery9-issue):


```
#define D3DISSUE_END (1 << 0) 
// Tells the runtime to issue the end of a query, changing its state to 
//   "non-signaled" 
```




```
 
#define D3DISSUE_BEGIN (1 << 1) // Tells the runtime to issue the 
// beginning of a query. 
```



Flags field for [**IDirect3DQuery9::GetData**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3dquery9-getdata):


```
 
#define D3DGETDATA_FLUSH (1 << 0) // Tells the runtime to flush 
// if the query is outstanding.
```



## Related topics

<dl> <dt>

[Programming Tips](programming-tips.md)
</dt> </dl>

 

 
