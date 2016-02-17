package example.bbFixedSequencer;

import easysim.Simulator;
import easysim.core.Node;

/**
 * Created by root on 17/02/16.
 */
public class FixedSequencer extends Node<FixedSequencerMessage> {

    private final int SEQUENCER_ID = 1;

    int nbReceivedMessages = 0;

    public FixedSequencer(String prefix) {
        super(prefix);
    }

    private Node<FixedSequencerMessage>[] getDestinations() {
        Node<FixedSequencerMessage>[] result = new Node[neighbors.length - 1];

        int index = 0;
        for (Node<FixedSequencerMessage> node : neighbors) {
            if (node.id != SEQUENCER_ID) {
                result[index] = node;
                index += 1;
            }
        }

        return result;
    }

    public void cycleHandler() {
        // Node 0 injects a new message in the system
        if (id == 4 && Simulator.getCycle() == 0) {
            send(new FixedSequencerMessage(), neighbors);
        }

        if (id == 2 && Simulator.getCycle() == 0) {
            send(new FixedSequencerMessage(), neighbors);
        }

        if (id == SEQUENCER_ID) {

            FixedSequencerMessage m;
            while ((m = receive()) != null) {
                nbReceivedMessages++;
                System.out.println("Sequencer received message from " + m.sendingNode);

                Node<FixedSequencerMessage>[] sendTo = getDestinations();
                send(m, sendTo);
            }
        } else {
            FixedSequencerMessage m;
            while ((m = receive()) != null) {
                nbReceivedMessages++;
            }
        }
    }

    @Override
    public String toString() {
        return "Example";
    }
}
