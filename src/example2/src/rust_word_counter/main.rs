use clap::Parser;
use std::collections::HashMap;
use std::fs;

#[derive(Parser)]
#[command(author, version, about, long_about = None)]
struct Args {
    file: String,
}

fn main() {
    let args = Args::parse();
    let content = fs::read_to_string(&args.file).expect("Could not read the file...");

    let mut frequencies = HashMap::new();

    for word in content.split_whitespace() {
        let word = word.to_lowercase();

        *frequencies.entry(word).or_insert(0) += 1;
    }

    let mut freq_vector: Vec<(&String, &i32)> = frequencies.iter().collect();
    freq_vector.sort_by(|a, b| b.1.cmp(a.1));

    for (word, count) in freq_vector {
        println!("{} : {} occurences", word, count);
    }
}
