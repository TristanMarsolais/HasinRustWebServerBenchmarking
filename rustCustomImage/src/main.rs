use pipelined_server::{setting::ServerSetting, pipeline::{default::{action::{generate_read_only_file_utility_thread, NO_BOUND}, self}, builder::pipeline::Builder, Server}};

const READ_THREAD_COUNT : usize = NO_BOUND;
const PIPELINE_COUNT : usize = 1;

fn main() {
    let setting = ServerSetting::load();
    println!("{setting:?}");

    let utility_thread = generate_read_only_file_utility_thread::<READ_THREAD_COUNT>();
        
    let builder = Builder::default()
        .set_settings(setting.clone())
        .set_parser(default::parser::<64, 1024>)
        .set_action(default::action)
        .set_compression(default::no_compression)
        .set_utility_thread(utility_thread.0.clone());

    let server = Server::new(setting, utility_thread, builder);

    println!("Starting server");
    server.run::<PIPELINE_COUNT>();
}
