```
// 어댑터 연결
recyclerView_plants = binding.calendarPlantsType;
layoutManager_plants = new LinearLayoutManager(getActivity(), RecyclerView.HORIZONTAL, false);
recyclerView_plants.setLayoutManager(layoutManager_plants);
adapter_plants = new CalendarPlantsAdapter(plantName[0], plantCreatedAt[0], plantHarvestTime[0]);
recyclerView_plants.setAdapter(adapter_plants);
```