#!/usr/bin/env python
# -*- coding: utf-8 -*-

import run
import scenario
import os
from utils import read_netlogo_file

agents = read_netlogo_file('tests/bwaise/agents.txt')

defences_to_breach = ["a"]

defences = read_netlogo_file('tests/bwaise/defences.txt')

roads = read_netlogo_file('tests/bwaise/roads.txt')

codes = read_netlogo_file('tests/bwaise/codes.txt')

terrain = read_netlogo_file('tests/bwaise/terrain.txt')

buildings = read_netlogo_file('tests/bwaise/preprocessed-buildings.txt')

streams = read_netlogo_file('tests/bwaise/streams.txt')


warning_times = ["07:50:00", "07:55:00", "08:00:00"]

sea_levels = [4]

if not os.path.exists('tests/outputs'):
    os.mkdir('tests/outputs')

model_path = 'tests/outputs/bwaise'
inputs_path = 'tests/bwaise'

scenarios = []

defence: str
for defence in defences_to_breach:
    for warning_time in warning_times:
        for sea_level in sea_levels:
            scenarios.append(
                scenario.Scenario(
                    path='tests/outputs/bwaise-defence-{}-evacuation-{}-sea-{}'.format(
                        defence, warning_time.replace(':', ''), sea_level),
                    width=220,
                    height=143,
                    start_time='7:45',
                    end_time='8:20',
                    agents=agents,
                    roads=roads,
                    codes=codes,
                    defences=defences,
                    buildings=buildings,
                    terrain=terrain,
                    streams=streams,
                    timeline=[[
                        ["0s",  1000, ["agent",  "kids"]],
                        ["06:05:00", ["sealevel",   1167]],
                        ["07:50:00", ["evacuate"]]
                    ]]
                ))

r = run.Run(scenarios=scenarios)

r.setup_and_run()
