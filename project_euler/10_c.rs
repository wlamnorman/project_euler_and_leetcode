fn primes_up_to(n: usize) -> Vec<usize> {
    let mut found_primes: Vec<usize> = Vec::new();

    'outer: for candidate in 2..=n {
        for &prime in &found_primes {
            if prime * prime > candidate {
                break;
            }
            if candidate % prime == 0 {
                continue 'outer;
            }
        }
        found_primes.push(candidate);
    }

    found_primes
}

fn main() {
    println!("{}", primes_up_to(2_000_000).iter().sum::<usize>());
}
