#!/usr/bin/env python

import argparse

from utils import dataset_reader
from utils import dataset_types
from utils import dict_utils

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str, help="Path to the track file", nargs="?")
    args = parser.parse_args()

    if args.filename is None:
        raise IOError("You must specify a filename. Type --help for help.")

    track_dictionary = dataset_reader.read_tracks(args.filename)

    print("Found " + str(len(track_dictionary)) + " object tracks.")
    for k, v in track_dictionary.items():
        print("Object ID: {} | Object Type: {}".format(k, v.agent_type))

    print("\nGet the track of the 1st object:")
    track = dict_utils.get_value_list(track_dictionary)[0]
    assert isinstance(track, dataset_types.Track)
    print("Track with id " + str(track.track_id) + " lasts from ts " + str(track.time_stamp_ms_first) + \
          " to ts " + str(track.time_stamp_ms_last) + ", so " +
          str((track.time_stamp_ms_last - track.time_stamp_ms_first) / 1000.) + " seconds.")

    init_motion_state = track.motion_states[track.time_stamp_ms_first]
    assert isinstance(init_motion_state, dataset_types.MotionState)
    print("Its initial motion state is " + str(init_motion_state))
    last_motion_state = track.motion_states[track.time_stamp_ms_last]
    assert isinstance(last_motion_state, dataset_types.MotionState)
    print("Its initial motion state is " + str(last_motion_state))


