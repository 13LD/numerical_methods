<?php
$x = [
    3.209,
    3.236,
    3.636,
    3.709,
    3.945
];

$y = [
    -12.472,
    -12.444,
    -11.004,
    -10.539,
    -8.677
];


$P = [];
$point = 3.923;
$n = 5;

for ($i = 0; $i < 5; $i++) {
    $P[$i][$i] = $y[$i];
}
for ($j =0; $j < $n; $j++) {
    for ($i = $j - 1; $i >= 0; $i--) {
        echo "$i;$j===========\n";
        $mult = 1 / ($x[$j] - $x[$i]);
        $P[$i][$j] = 1;
        echo "1 / ({$x[$j]} - {$x[$i]})\n";
        echo "{$point} - {$x[$i]};  {$P[$i][$j-1]}\n";
        echo "{$point} - {$x[$j]};  {$P[$i + 1][$j]}\n";
        $det = ((($point - $x[$i]) *  ($P[$i + 1][$j])) - ($P[$i][$j-1] * ($point - $x[$j])));
        echo "{$det} / " . ($x[$j] - $x[$i]) .  "\n";
        $P[$i][$j] = $mult * ((($point - $x[$i]) *  ($P[$i + 1][$j])) - ($P[$i][$j-1] * ($point - $x[$j])));
        echo "{$P[$i][$j]}\n";
    }
}

var_dump($P[0][$n - 1]);